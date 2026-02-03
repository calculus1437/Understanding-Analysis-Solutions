import PyPDF2
import re

def extract_chapter_6(pdf_path):
    print(f"Opening {pdf_path}...")
    try:
        reader = PyPDF2.PdfReader(pdf_path)
        num_pages = len(reader.pages)
        print(f"Total pages: {num_pages}")
        
        found_start = False
        extracted_text = []
        
        # Heuristic: Look for "Chapter 6" or specific Exercise 6.X.X patterns
        # Adjust range if needed. Usually Chapter 6 is in the middle.
        for i in range(num_pages):
            text = reader.pages[i].extract_text()
            
            # Simple state machine to find Chapter 6
            if "Chapter 6" in text or "Sequences and Series of Functions" in text:
                found_start = True
                print(f"Found Chapter 6 start on page {i+1}")
            
            if "Chapter 7" in text and found_start:
                 print(f"Found Chapter 7 start on page {i+1}, stopping.")
                 break
            
            if found_start:
                extracted_text.append(text)
                
        return "\n".join(extracted_text)

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    pdf_path = r"c:\Users\calculus\Desktop\电子书\UA_Solutions.pdf"
    content = extract_chapter_6(pdf_path)
    
    # Save to a file for review
    with open(r"c:\Users\calculus\Desktop\MathNotes\scripts\ua_ch6_raw.txt", "w", encoding="utf-8") as f:
        f.write(content)
    
    print("Extraction complete. check ua_ch6_raw.txt")
