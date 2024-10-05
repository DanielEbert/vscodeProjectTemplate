import inquirer

def main():
    questions = [
        inquirer.Checkbox(
            "interests",
            message="What are you interested in?",
            choices=["Computers", "Books", "Science", "Nature", "Fantasy", "History"],
            default=["Computers", "Books"],
        ),
    ]

    answers = inquirer.prompt(questions)

    print(answers)


if __name__ == '__main__':
    raise SystemExit(main())
