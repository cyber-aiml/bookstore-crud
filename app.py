import streamlit as st
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

API_URL = "http://localhost:8000"

def get_books():
    try:
        response = requests.get(f"{API_URL}/books/")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logger.error(f"Error fetching books: {e}")
        st.error("Failed to fetch books.")
        return []

def create_book(name, summary, price, quantity, author):
    try:
        book = {
            "name": name,
            "summary": summary,
            "price": price,
            "quantity": quantity,
            "author": author
        }
        response = requests.post(f"{API_URL}/books/", json=book)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logger.error(f"Error creating book: {e}")
        st.error("Failed to create book.")
        return None

def update_book_quantity(book_id, quantity):
    try:
        response = requests.put(f"{API_URL}/books/{book_id}", json={"quantity": quantity})
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logger.error(f"Error updating book quantity: {e}")
        st.error("Failed to update book quantity.")
        return None

def delete_book(book_id):
    try:
        response = requests.delete(f"{API_URL}/books/{book_id}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logger.error(f"Error deleting book: {e}")
        st.error("Failed to delete book.")
        return None

st.title("Bookstore Inventory")

menu = ["View Books", "Add Book", "Update Book Quantity", "Delete Book"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "View Books":
    st.subheader("All Books")
    books = get_books()
    if len(books) != 0:
        st.table(books)

elif choice == "Add Book":
    st.subheader("Add a New Book")
    name = st.text_input("Name")
    summary = st.text_area("Summary")
    price = st.number_input("Price", min_value=0.0, format="%.2f")
    quantity = st.number_input("Quantity", min_value=0)
    author = st.text_input("Author")
    if st.button("Add Book"):
        new_book = create_book(name, summary, price, quantity, author)
        if new_book:
            st.success(f"Added book: {new_book['name']}")

elif choice == "Update Book Quantity":
    st.subheader("Update Book Quantity")
    book_id = st.number_input("Book ID", min_value=0)
    quantity = st.number_input("Quantity", min_value=0)
    if st.button("Update Quantity"):
        updated_book = update_book_quantity(book_id, quantity)
        if updated_book:
            st.success(f"Updated book: {updated_book['name']} to quantity {updated_book['quantity']}")

elif choice == "Delete Book":
    st.subheader("Delete a Book")
    book_id = st.number_input("Book ID", min_value=0)
    if st.button("Delete Book"):
        deleted_book = delete_book(book_id)
        if deleted_book:
            st.success(f"Deleted book: {deleted_book['name']}")
