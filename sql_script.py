import csv

table_name = "projects"


def generate_commands(filename):
    reader = csv.reader(open(filename, "r"))

    f = open("new_sql_script.sql", "w")
    next(reader) # skipping header
    for row in reader:
        project_id, project_title, availability, description, sdg, faculty_name, college_email, mobile_number, department = row

        command = (f"INSERT INTO {table_name} VALUES (\"{project_id}\", \"{project_title}\", {availability}, \"{description}\", \"{sdg}\", \"{faculty_name}\", \"{college_email}\", \"{mobile_number}\", \"{department}\");\n")

        command.replace("'", "''") # escaping single quote character in command

        command.replace("\"", "'")

        f.write(command)
        print(command)

generate_commands('azure_db_projects.csv')
    