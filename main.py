from parser import parse_input
from query_builder import generate_sql
from executor import execute_query

def main():
    print("Smart SQL Generator (PostgreSQL)\n")

    while True:
        user_input = input("Enter query: ")

        if user_input.lower() == "exit":
            break

        parsed = parse_input(user_input)
        sql_query = generate_sql(parsed)

        print("\nGenerated SQL:", sql_query)

        results = execute_query(sql_query)

        print("\nResults:")
        for row in results:
            print(row)

if __name__ == "__main__":
    main()