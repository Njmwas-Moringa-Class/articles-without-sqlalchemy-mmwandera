from Author import Author
from Magazine import Magazine
from Article import Article

def display_options():
    print("\nOptions:")
    print("1. Add Author")
    print("2. Add Magazine")
    print("3. Add Article")
    print("4. Get Author Info")
    print("5. Get Magazine Info")
    print("6. Print All Authors")
    print("7. Print All Magazines")
    print("8. Exit")

def add_author():
    author_name = input("Enter author's name: ")
    Author(author_name)
    print(f"Author '{author_name}' added.")

def add_magazine():
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    Magazine(magazine_name, magazine_category)
    print(f"Magazine '{magazine_name}' added.")

def add_article():
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")

    author = Author.find_or_create(author_name)
    magazine = Magazine.find_or_create(magazine_name, magazine_category)

    author.add_article(magazine, article_title)
    print(f"Article '{article_title}' added to {magazine_name} by {author_name}.")

def get_author_info():
    author_name = input("Enter author's name: ")
    author = Author.find_by_name(author_name)

    if author:
        print(f"Author Info:\nName: {author.name}")
        print(f"Articles: {[article.title for article in author.articles()]}")
        print(f"Magazines: {[magazine.name for magazine in author.magazines()]}")
        print(f"Topic Areas: {author.topic_areas()}")
    else:
        print(f"Author '{author_name}' not found.")

def get_magazine_info():
    magazine_name = input("Enter magazine name: ")
    magazine = Magazine.find_by_name(magazine_name)

    if magazine:
        print(f"Magazine Info:\n{magazine}")
        print(f"Contributors: {[author.name for author in magazine.contributors()]}")
        print(f"Article Titles: {magazine.article_titles()}")
        print(f"Contributing Authors (more than 2 articles): {magazine.contributing_authors()}")
    else:
        print(f"Magazine '{magazine_name}' not found.")

def print_all_authors():
    print("\nAll Authors:")
    for author in Author.all():
        print(f"{author.name}")

def print_all_magazines():
    print("\nAll Magazines:")
    for magazine in Magazine.all():
        print(magazine)

def main():
    while True:
        display_options()
        choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")

        if choice == "1":
            add_author()
        elif choice == "2":
            add_magazine()
        elif choice == "3":
            add_article()
        elif choice == "4":
            get_author_info()
        elif choice == "5":
            get_magazine_info()
        elif choice == "6":
            print_all_authors()
        elif choice == "7":
            print_all_magazines()
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, 7, or 8.")

if __name__ == "__main__":
    main()
