"""
Bug Report Automation Script
Author: Md. Nazmus Shakib
Description: This script stores all detected bugs in a structured format,
prints them in the console in a readable way, and automatically generates
an Excel file (Bug_Report_Md. Nazmus Shakib.xlsx) for review or sharing.
"""

import os
import sys
import pandas as pd
import datetime
import textwrap

# Base directory setup
if getattr(sys, "frozen", False):
    BASE_DIR = os.path.dirname(os.path.dirname(sys.executable))
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SCREENSHOT_DIR = os.path.join(BASE_DIR, "screenshots")
VIDEO_DIR = os.path.join(BASE_DIR, "videos")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)
os.makedirs(VIDEO_DIR, exist_ok=True)

# Bug data
bugs = [
    {
        "BUG-ID": "BUG - 001",
        "Title": "Page fails to load",
        "Description": "Page fails to load after too many requests. Server returns HTTP 429",
        "Category": "Functional",
        "Steps to Reproduce": "1. Open page on desktop\n2.Perform multiple requests quickly\n3. Observe error",
        "Expected Result": "Page should load without errors or server should handle high request rate gracefully.",
        "Actual Result": "Page fails to load, shows 429 Too Many Requests.",
        "Severity": "High",
        "Screenshot": os.path.join(SCREENSHOT_DIR, "HTTP 429 code.JPG"),
    },
    {
        "BUG-ID": "BUG - 002",
        "Title": "Slow loading",
        "Description": "sorbosesh news part/Sorbadhik pothito section slow loading both on desktop/mobile devices.",
        "Category": "Performance",
        "Steps to Reproduce": "1. Open Home page\n2. Go to the sorbosesh news part/Sorbadhik pothito section\n3. Observe slower content loading",
        "Expected Result": "Section contents should load at the same speed like other parts",
        "Actual Result": "Content starts slow loading making more time delay to load these sorbosesh news part/Sorbadhik pothito sections.",
        "Severity": "Medium",
        "Screenshot": os.path.join(SCREENSHOT_DIR, "sorbosesh news partSorbadhik pothito section.JPG"),
    },
    {
        "BUG-ID": "BUG - 003",
        "Title": "Links and Sections do not appear",
        "Description": "Certain links and sections do not appear on mobile on first load, but becomes visible or perfectly workable after switching between desktop and mobile views. similar issues observed for multiple sections on both desktop and mobile.",
        "Category": "Functional",
        "Steps to Reproduce": "1. Open page on mobile view/desktop view -> some sections missing\n2. Switch views and come back again to previous views\n3. Missing links or contents are now working or available perfectly",
        "Expected Result": "All links and content should display correctly on first load, Regardless of device or viewport changes.",
        "Actual Result": "Some of the links and content gets disappeared because of switching viewport back and forth.",
        "Severity": "Medium",
        "video": os.path.join(VIDEO_DIR, "links and content disappear.mp4"),
    },
    {
        "BUG-ID": "BUG - 004",
        "Title": "Dark mode UI not appropriate",
        "Description": "When viewing the website from chrome's dark mode, the UI colors appear mismatched - Logo, text, background, and elements look not so nice and headings of news also can’t be understood or viewed clearly as well.",
        "Category": "UI/Design",
        "Steps to Reproduce": "1. Open chrome\n2. Go to appearance from the chrome bottom pen icon\n3. After switching to dark mode, view the website\n4. Observe colors and texts of heading news and other parts.",
        "Expected Result": "UI should remain visually consistent and readable in both light and dark modes.",
        "Actual Result": "Website UI breaks in dark mode - color contrast and design look incorrect.",
        "Severity": "Medium",
        "video": os.path.join(VIDEO_DIR, "Website UI distorted in dark mode.mp4"),
    },
    {
        "BUG-ID": "BUG - 005",
        "Title": "Paragraph view overlaps with line separator",
        "Description": "When viewing the home page headline news, the sub-heading paragraph view overlaps with the below separator line for desktop.",
        "Category": "UI/Design",
        "Steps to Reproduce": "1. Open website\n2. Wait for heading news to load\n3. See 2nd or 3rd news — the sub-heading overlaps with the bottom line.",
        "Expected Result": "The sub-heading paragraph text should not overlap the bottom separator line.",
        "Actual Result": "Paragraph text overlaps with the bottom separator line.",
        "Severity": "Medium",
        "Screenshot": os.path.join(SCREENSHOT_DIR, "subheading paragraph overlaps bottom line.JPG"),
    },
    {
        "BUG-ID": "BUG - 006",
        "Title": "Paragraph overlaps with ad banner",
        "Description": "In desktop view, the news content text (paragraph section) overlaps with the advertisement banner placed below. The overlap causes text to be hidden and unreadable, especially in sections with more than 3 headlines.",
        "Category": "UI/Design",
        "Steps to Reproduce": "1. Open website\n2. Go to the 'Any news' section\n3. Browse using the next button.",
        "Expected Result": "Paragraph text should not overlap the advertisement banner.",
        "Actual Result": "Paragraph text overlaps with the ad banner.",
        "Severity": "Medium",
        "Screenshot": os.path.join(SCREENSHOT_DIR, "Rangamati news overlaps ad banner.JPG"),
    },
    {
        "BUG-ID": "BUG - 007",
        "Title": "Extra news creates blank space on left side",
        "Description": "In desktop view, once you open 'any news' and click 'Read more', it creates an absurd blank space on the left side of the page above the footer.",
        "Category": "UI/Design",
        "Steps to Reproduce": "1. Open website\n2. Go to the 'Any news' section\n3. Click the 'Aro Porun / Read more' button\n4. Observe the empty left space above footer.",
        "Expected Result": "The view should not create blank space after clicking 'Read more'.",
        "Actual Result": "It creates a blank space on the left after clicking 'Read more'.",
        "Severity": "Low",
        "Screenshot": os.path.join(SCREENSHOT_DIR, "Odd UI empty section.JPG"),
    },
]

# ---------- Display Function ----------

def display_bug():
    def indent_multiline(label, text, width=90, pad=20):
        
        wrapper = textwrap.TextWrapper(width=width,
        subsequent_indent=" " * (pad + 5))
        wrapped = wrapper.fill(str(text))
        return f"{label:<{pad}} :  {wrapped}"

    print("\n=== BUG REPORT SUMMARY ===\n")

    for bug in bugs:
        print(f"{'BUG ID':<20} :   {bug.get('BUG-ID')}")
        print(f"{'Title':<20} :   {bug.get('Title')}")
        print(indent_multiline("Description", bug.get("Description", "")))
        print(f"{'Category':<20} :   {bug.get('Category')}")
        print(indent_multiline("Steps to Reproduce", bug.get("Steps to Reproduce", "")))
        print(indent_multiline("Expected Result", bug.get("Expected Result", "")))
        print(indent_multiline("Actual Result", bug.get("Actual Result", "")))
        print(f"{'Severity':<20} :   {bug.get('Severity')}")
        if bug.get("Screenshot"):
            print(f"{'Screenshot':<20} :   {bug.get('Screenshot')}")
        if bug.get("video"):
            print(f"{'video':<20} :   {bug.get('video')}")
        print("-" * 60)


# ---------- Excel Export ----------
def export_to_excel():
    df = pd.DataFrame(bugs)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    desktop_dir = os.path.join(os.path.expanduser("~"), "Desktop")
    output_file = os.path.join(desktop_dir, f"Bug_Report_Md_Nazmus_Shakib_{timestamp}.xlsx")
    df.to_excel(output_file, index=False)
    print(f"\nExcel file created successfully!'{output_file}'")

# ---------- Main ----------
if __name__ == "__main__":
    display_bug()
    export_to_excel()
    input("\nPress Enter to exit....")
