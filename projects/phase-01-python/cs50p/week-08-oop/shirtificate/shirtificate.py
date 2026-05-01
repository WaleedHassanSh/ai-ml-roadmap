# A program that generates a personalized CS50 shirtificate PDF.

from fpdf import FPDF


def main():
    name = input("Name: ")

    pdf = FPDF(orientation="portrait", format="A4")
    pdf.set_auto_page_break(False)
    pdf.add_page()
    pdf.set_font("helvetica", style="B", size=30)
    pdf.cell(text="CS50 Shirtificate", w=0, h=20, align="C")
    pdf.image("shirtificate.png", x=10, y=70, w=190)
    pdf.set_font("helvetica", style="B", size=24)
    pdf.set_y(130)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(w=0, h=10, text=f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
