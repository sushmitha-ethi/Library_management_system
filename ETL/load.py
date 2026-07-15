import psycopg2

# DB Connection
def get_connection():
    return psycopg2.connect(
        dbname="library_db",
        user="postgres",
        password="Senpai",
        host="localhost"
    )


#  LOAD MEMBERS (FINAL VERSION)
def load_members(df):
    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        inserted = 0
        skipped = 0

        for _, row in df.iterrows():

            #  Clean + validate email
            email = str(row['email']).strip()

            if not email:
                skipped += 1
                continue

            #  Case-insensitive duplicate check
            cursor.execute(
                "SELECT 1 FROM members WHERE LOWER(email)=LOWER(%s)",
                (email,)
            )

            if cursor.fetchone():
                skipped += 1
                continue

            cursor.execute("""
                INSERT INTO members (name, email, phone, address)
                VALUES (%s, %s, %s, %s)
            """, (
                row['name'],
                email,
                row['phone'],
                row['address']
            ))

            inserted += 1

        conn.commit()

        print(f" Members --- Inserted: {inserted}, Skipped: {skipped}")

    except Exception as e:
        print(f" Members Load Error: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


#  LOAD BOOKS (FINAL VERSION)
def load_books(df):
    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        inserted = 0
        skipped = 0

        for _, row in df.iterrows():

            # Clean + validate title
            title = str(row['title']).strip()

            if not title:
                skipped += 1
                continue

            #  Case-insensitive duplicate check
            cursor.execute(
                "SELECT 1 FROM books WHERE LOWER(title)=LOWER(%s)",
                (title,)
            )

            if cursor.fetchone():
                skipped += 1
                continue

            cursor.execute("""
                INSERT INTO books (
                    title, author, publisher, publication_year, category, copies_available
                )
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                title,
                row['author'],
                row['publisher'],
                row['publication_year'],
                row['category'],
                row['copies']
            ))

            inserted += 1

        conn.commit()

        print(f" Books --- Inserted: {inserted}, Skipped: {skipped}")

    except Exception as e:
        print(f" Books Load Error: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()