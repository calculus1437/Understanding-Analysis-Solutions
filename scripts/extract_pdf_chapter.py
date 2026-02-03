import PyPDF2
import re

def extract_text_from_pdf(pdf_path, search_term="5.4", context_pages=5):
    print(f"Opening {pdf_path}...")
    try:
        reader = PyPDF2.PdfReader(pdf_path)
        num_pages = len(reader.pages)
        print(f"Total pages: {num_pages}")
        
        found_content = []
        
        for i in range(num_pages):
            page_text = reader.pages[i].extract_text()
            if "练习 5.4" in page_text or "习题 5.4" in page_text:
                print(f"Found keyword on page {i + 1}")
                # Extract this page and maybe the next few pages
                for j in range(i, min(i + context_pages, num_pages)):
                    text = reader.pages[j].extract_text()
                    found_content.append(f"--- Page {j + 1} ---\n{text}\n")
                break # Assuming we found the section start
        
        return "".join(found_content)

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    pdf_path = r"c:\Users\calculus\Desktop\电子书\patched_Understanding Analysis(中译本) (Stephen Abbott) (Z-Library).pdf"
    content = extract_text_from_pdf(pdf_path, "练习 5.4")
    print("Extracted Content Preview:")
    print(content)
