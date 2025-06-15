import tkinter as tk
from tkinter import *
from tkinter import Tk, Label, Button, Radiobutton, IntVar, Frame, Entry
import random
from PIL import Image, ImageTk
import sqlite3
from tkinter import ttk

def create_database():
    conn = sqlite3.connect("quiz_results.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS quiz_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            rollno TEXT NOT NULL UNIQUE,
            course TEXT NOT NULL,
            branch TEXT NOT NULL,
            marks INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

create_database()

# Fetch and display stored quiz results
conn = sqlite3.connect("quiz_results.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM quiz_results")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()

# GUI Setup
BG_COLOR = "#D6E1A7" 
BG_COLOR2 = "#fff" #white
BOX_COLOR = "#CEE8FA"

ACCENT_COLOR="#577C8E"
BTN_COLOR = "#2F4157"
HEADER_COLOR = "#2F4157" #same as btn_color
TEXT_COLOR = "#333333" #black

DISABLED_COLOR = "#A5A5A5" #grey
WARNING_COLOR = "#EE7A13" #red

HEADER_FONT = ("Georgia", 24, "bold")
HEADER_MID_FONT = ("Georgia", 18, "bold")

TEXT_BIGGER_FONT = ("Montserrat", 18, "bold")
TEXT_BIG_FONT = ("Montserrat", 16, "bold")
TEXT_MID_FONT = ("Montserrat", 14, "bold")
TEXT_SMALL_FONT = ("Montserrat", 12)
TEXT_SMALLER_FONT = ("Montserrat", 8)

BTN_FONT = ("Montserrat", 14, "bold")
OPT_FONT = ("Montserrat", 14)

# Questions and Answers
questions = [
    "Total keywords in Python?",
    "Which function takes a console input in Python?",
    "Output of 2**3?",
    "Which of the following is necessary to execute Python code?",
    "Output of np.arange(1,5)?",
    "The append method adds value to the list at the?",
    "Keyword used to declare a function?",
    "Output of 2*21?",
    "Which keyword is used to create a function in Python?",
    "To declare a global variable in Python we use the keyword?"
]

answer_choice = [
    ['33', '31', '30', '32'],
    ['get()', 'input()', 'gets()', 'scan()'],
    ['6', '8', '9', '12'],
    ['TURBO C', 'Py Interpreter', 'Notepad', 'IDE'],
    ['[1,2,3,4]', '[0,1,2,3,4]', '[1,2,3,4,5]', '[2,4,5,1,3]'],
    ['custom location', 'end', 'center', 'beginning'],
    ['define', 'dif', 'def', 'null'],
    ['28', '24', '42', '32'],
    ['function', 'void', 'fun', 'def'],
    ['all', 'var', 'let', 'global']
]


answers = [0, 1, 1, 1, 0, 1, 2, 2, 3, 3]

# Initialize main window
root = tk.Tk()
root.title('Python Quiz')
root.geometry("1300x800")
root.config(background=BG_COLOR)
root.resizable(True, True)

indexes = random.sample(range(10), 5)
user_answers = [-1] * 5
ques = 0
username = ""
rollno = ""
course = ""
branch = ""

# Start Frame (Centered)
start_frame = Frame(root, bg=BG_COLOR2, padx=120, pady=20)
start_frame.place(relx=0.5, rely=0.5, anchor="center")

# Head Frame
start_frame_head = Frame(start_frame, bg=BG_COLOR2)
start_frame_head.grid(row=0, column=0, columnspan=2, pady=10)

logo_path = "logo.png"
original_logo = Image.open(logo_path)
resized_logo = original_logo.resize((150, 150), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(resized_logo)

image_label = Label(start_frame_head, image=img, bg=BG_COLOR2)
image_label.image = img
image_label.grid(row=0, column=0, pady=10)

title_label = Label(start_frame_head, text="Python Quiz", font=HEADER_FONT, bg=BG_COLOR2, fg=HEADER_COLOR)
title_label.grid(row=1, column=0, padx=20, pady=20)

# Body Frame (Input Fields)
start_frame_body = Frame(start_frame, bg=BG_COLOR2)
start_frame_body.grid(row=1, column=0, columnspan=2, pady=20)
start_frame_body.columnconfigure(0, weight=1, minsize=150)
start_frame_body.columnconfigure(1, weight=2, minsize=200)

# Name Entry
name_label = Label(start_frame_body, text="Enter your name:", font=TEXT_MID_FONT, bg=BG_COLOR2)
name_label.grid(row=0, column=0, sticky="w", pady=5, padx=10)
name_entry = Entry(start_frame_body, font=TEXT_MID_FONT, width=20)
name_entry.grid(row=0, column=1, pady=5, padx=10, sticky="ew")
name_warning = Label(start_frame_body, text="", font=TEXT_SMALLER_FONT, fg=WARNING_COLOR, bg=BG_COLOR2)
name_warning.grid(row=1, column=1, sticky="w")

# Roll No Entry
rollno_label = Label(start_frame_body, text="Enter Roll No:", font=TEXT_MID_FONT, bg=BG_COLOR2)
rollno_label.grid(row=2, column=0, sticky="w", pady=5, padx=10)
rollno_entry = Entry(start_frame_body, font=TEXT_MID_FONT, width=20)
rollno_entry.grid(row=2, column=1, pady=5, padx=10, sticky="ew")
rollno_warning = Label(start_frame_body, text="", font=TEXT_SMALLER_FONT, fg=WARNING_COLOR, bg=BG_COLOR2)
rollno_warning.grid(row=3, column=1, sticky="w")

# Course Selection
course_label = Label(start_frame_body, text="Course:", font=TEXT_MID_FONT, bg=BG_COLOR2)
course_label.grid(row=4, column=0, sticky="w", pady=5, padx=10)
course_var = StringVar(value="Select Course")
course_menu = OptionMenu(start_frame_body, course_var, "Select Course", "BTech", "MTech")
course_menu.config(font=TEXT_MID_FONT, width=15)
course_menu.grid(row=4, column=1, pady=5, padx=10, sticky="ew")
course_warning = Label(start_frame_body, text="", font=TEXT_SMALLER_FONT, fg=WARNING_COLOR, bg=BG_COLOR2)
course_warning.grid(row=5, column=1, sticky="w")

# Branch Selection
branch_label = Label(start_frame_body, text="Branch:", font=TEXT_MID_FONT, bg=BG_COLOR2)
branch_label.grid(row=6, column=0, sticky="w", pady=5, padx=10)
branch_var = StringVar(value="Select Branch")
branch_menu = OptionMenu(start_frame_body, branch_var, "Select Branch", "CSE", "IT", "ECE", "ME", "EE")
branch_menu.config(font=TEXT_MID_FONT, width=15)
branch_menu.grid(row=6, column=1, pady=5, padx=10, sticky="ew")
branch_warning = Label(start_frame_body, text="", font=TEXT_SMALLER_FONT, fg=WARNING_COLOR, bg=BG_COLOR2)
branch_warning.grid(row=7, column=1, sticky="w")

# Centering Start Button
start_btn = Button(start_frame, text="Start Quiz", font=BTN_FONT, bg=HEADER_COLOR, fg=BG_COLOR2, command=lambda: startIspressed())
start_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, sticky="ew")
 


def startIspressed():
    global start_frame, username, rollno, branch, course
    username = name_entry.get().strip()
    rollno = rollno_entry.get().strip()
    branch = branch_var.get().strip()
    course = course_var.get().strip()

    # Reset warning messages
    name_warning.config(text="")
    rollno_warning.config(text="")
    course_warning.config(text="")
    branch_warning.config(text="")

    has_error = False

    if not username or not username.isalpha():
        name_warning.config(text="* Required field, Alphabets Only", fg=WARNING_COLOR)
        has_error = True
    if not rollno.isdigit():
        rollno_warning.config(text="* Numbers only", fg=WARNING_COLOR)
        has_error = True
    if course == "Select Course":
        course_warning.config(text="* Please select a course", fg=WARNING_COLOR)
        has_error = True
    if branch == "Select Branch":
        branch_warning.config(text="* Please select a branch", fg=WARNING_COLOR)
        has_error = True
    if has_error:
        return
    
    # Database Insertion
    try:
        conn = sqlite3.connect("quiz_results.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO quiz_results (name, rollno, course, branch, marks) VALUES (?, ?, ?, ?, ?)",
                       (username, rollno, course, branch, 0))
        conn.commit()
        conn.close()
    except sqlite3.IntegrityError:
        rollno_warning.config(text="* Roll No already exists!", fg=WARNING_COLOR)
        return

    start_frame.destroy()
    startquiz()
    
# Global question tracker
total_questions = 5
ques = 0
user_answers = [-1] * total_questions
marked_questions = set()
viewed_questions = set()
nav_buttons = {}
def startquiz():
    """Initializes and displays the quiz interface."""
    global lblQuestion, r1, r2, r3, r4, radiovar, question_tracker, btnNext, btnPrev
    global main_frame
    global attempted_label, marked_label, skipped_label
    
    viewed_questions.add(ques)
    # Main Quiz Frame
    main_frame = Frame(root, bg=BG_COLOR)
    main_frame.grid(row=0, column=0, sticky="nsew")
    main_frame.grid_rowconfigure(0, weight=1)
    main_frame.grid_columnconfigure(0, weight=1)

    # Configure column proportions for even spacing
    main_frame.grid_columnconfigure(0, weight=3)
    main_frame.grid_columnconfigure(1, weight=1) 
    
    quiz_frame = Frame(main_frame, bg=BG_COLOR2, padx=20, pady=20)
    quiz_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    # Tracker Frame
    tracker_frame = Frame(quiz_frame, bg=BG_COLOR2, padx=10, pady=10)
    tracker_frame.grid(row=0, column=0, padx=20, pady=20)
    question_tracker = Label(tracker_frame, text=f"Question {ques+1}/{total_questions}", font=TEXT_BIG_FONT, bg=BG_COLOR2, fg=DISABLED_COLOR)
    question_tracker.grid(row=0, column=0, pady=10, sticky="ew")
    
    lblQuestion = Label(
    quiz_frame, 
    text=questions[indexes[ques]], 
    font=TEXT_BIGGER_FONT, 
    height=2, 
    justify="left", 
    background=BG_COLOR2, 
    fg=HEADER_COLOR, 
    anchor="w",
    wraplength=650
    )
    lblQuestion.grid(row=1, column=0, columnspan=2, pady=10, sticky="w")

    
    radiovar = IntVar()
    radiovar.set(user_answers[ques])
    option_style = {
        "font": OPT_FONT, "variable": radiovar, "background": BOX_COLOR,
        "width": 60, "height": 2, "anchor": "w", "indicatoron": 0,
        "selectcolor": ACCENT_COLOR
    }
    r1 = Radiobutton(quiz_frame, text=answer_choice[indexes[ques]][0], value=0, **option_style)
    r2 = Radiobutton(quiz_frame, text=answer_choice[indexes[ques]][1], value=1, **option_style)
    r3 = Radiobutton(quiz_frame, text=answer_choice[indexes[ques]][2], value=2, **option_style)
    r4 = Radiobutton(quiz_frame, text=answer_choice[indexes[ques]][3], value=3, **option_style)
    
    r1.grid(row=3, column=0, padx=5, pady=5, sticky="w")
    r2.grid(row=4, column=0, padx=5, pady=5, sticky="w")
    r3.grid(row=5, column=0, padx=5, pady=5, sticky="w")
    r4.grid(row=6, column=0, padx=5, pady=5, sticky="w")

    # Navigation Buttons
    btn_frame = Frame(quiz_frame, bg=BG_COLOR2)
    btn_frame.grid(row=8, column=0, columnspan=2, pady=20, sticky="ew")
    
    # Configure btn_frame columns for spacing
    btn_frame.grid_columnconfigure(0, weight=1)
    btn_frame.grid_columnconfigure(1, weight=1)
    # Left Frame (Mark, Prev, Next)
    left_frame = Frame(btn_frame, bg=BG_COLOR2)
    left_frame.grid(row=0, column=0, sticky="w")
    btnMark = Button(left_frame, text="Mark For Review", font=BTN_FONT, bg=BTN_COLOR, fg=BG_COLOR2, width=14, command=mark_for_review)
    btnMark.grid(row=0, column=0, padx=2, pady=3)
    btnPrev = Button(left_frame, text="<", font=BTN_FONT, bg=BTN_COLOR, fg=BG_COLOR2, width=7, command=lambda: navigate_question(-1, radiovar))
    btnPrev.grid(row=0, column=1, padx=2, pady=3)
    btnNext = Button(left_frame, text=">", font=BTN_FONT, bg=BTN_COLOR, fg=BG_COLOR2, width=7, command=lambda: navigate_question(1, radiovar))
    btnNext.grid(row=0, column=2, padx=2, pady=3)
    # Finish Button - Aligned to the right
    btnFinish = Button(btn_frame, text="Finish", font=BTN_FONT, bg=BTN_COLOR, fg=BG_COLOR2, width=14, command=lambda: finish_test())
    btnFinish.grid(row=0, column=1, padx=2, pady=3, sticky="e")

    # Side Frame
    side = Frame(main_frame, bg=BG_COLOR2, padx=20, pady=20)
    side.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
    
    student_frame = tk.Frame(side, bg=BG_COLOR2)
    student_frame.grid(row=0, column=0, columnspan=4, pady=10, sticky="ew")
    student_name_label = tk.Label(student_frame, text=f"STUDENT: {username}", bg=BG_COLOR2, font=HEADER_MID_FONT, height=2)
    student_name_label.grid(row=0, column=0, columnspan=4, padx=15, pady=15, sticky="nw")
    student_rollno_label = tk.Label(student_frame, text=f"ROLL NO: {rollno}", bg=BG_COLOR2, font=TEXT_SMALL_FONT)
    student_rollno_label.grid(row=1, column=0, columnspan=4, padx=15, pady=4, sticky="nw")
    student_course_label = tk.Label(student_frame, text=f"COURSE: {course}", bg=BG_COLOR2, font=TEXT_SMALL_FONT)
    student_course_label.grid(row=2, column=0, columnspan=4, padx=15, pady=4, sticky="nw")
    student_branch_label = tk.Label(student_frame, text=f"BRANCH: {branch}", bg=BG_COLOR2, font=TEXT_SMALL_FONT)
    student_branch_label.grid(row=3, column=0, columnspan=4, padx=15, pady=4, sticky="nw")

    ribbon_frame = tk.Frame(side, bg=BG_COLOR2)
    ribbon_frame.grid(row=1, column=0, columnspan=4, pady=10, sticky="ew")
    attempted_label = tk.Label(ribbon_frame, text="Attempted: 0", bg="green", fg="white", width=15, font=TEXT_SMALL_FONT)
    attempted_label.grid(row=0, column=0, padx=5, pady=5)
    marked_label = tk.Label(ribbon_frame, text="Marked: 0", bg="orange", fg="white", width=15, font=TEXT_SMALL_FONT)
    marked_label.grid(row=0, column=1, padx=5, pady=5)
    skipped_label = tk.Label(ribbon_frame, text="Skipped: 0", bg="pink", fg="white", width=15, font=TEXT_SMALL_FONT)
    skipped_label.grid(row=0, column=2, padx=5, pady=5)

    nav_grid = Frame(side, bg=BG_COLOR2, padx=20, pady=20)
    nav_grid.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="n")
    rows = (total_questions // 5) + (1 if total_questions % 5 else 0)
    cols = min(5, total_questions)
    for i in range(rows):
        for j in range(cols):
            num = i * 5 + j
            if num >= total_questions:
                break
            
            btn = Button(nav_grid, text=str(num+1), width=5, height=1, bg=BOX_COLOR, command=lambda q=num+1: navigate_to_question(q))
            btn.grid(row=i, column=j, padx=5, pady=2)
            nav_buttons[num] = btn

    update_buttons()
    update_ribbon()
    
    
def navigate_to_question(q_num):
    """Navigates directly to the selected question from the grid."""
    global ques  
    viewed_questions.add(ques)
    
    update_nav_button(ques)
    user_answers[ques] = radiovar.get()
    ques = q_num - 1

    question_tracker.config(text=f"Question {ques+1}/{total_questions}")
    lblQuestion.config(text=questions[indexes[ques]])
    r1.config(text=answer_choice[indexes[ques]][0], value=0)
    r2.config(text=answer_choice[indexes[ques]][1], value=1)
    r3.config(text=answer_choice[indexes[ques]][2], value=2)
    r4.config(text=answer_choice[indexes[ques]][3], value=3)

    radiovar.set(user_answers[ques] if user_answers[ques] != -1 else -1)

    update_buttons()
    update_ribbon()
    root.update_idletasks()
 
        
def mark_for_review():
    """Marks the current question for review and updates the tracker button color."""
    global ques
    if ques in marked_questions:
        marked_questions.remove(ques)
    else:
        marked_questions.add(ques)

    update_ribbon()
    update_nav_button(ques)


def navigate_question(direction, radiovar):
    """Handles navigating between questions."""
    global ques  
    viewed_questions.add(ques)
    user_answers[ques] = radiovar.get()
    
    update_nav_button(ques)
    if direction == 1 and ques < total_questions - 1:
        ques += 1
    elif direction == -1 and ques > 0:
        ques -= 1
    elif direction == 1 and ques == total_questions - 1:
        calc()  
        return  

    question_tracker.config(text=f"Question {ques+1}/{total_questions}")
    lblQuestion.config(text=questions[indexes[ques]])
    r1.config(text=answer_choice[indexes[ques]][0], value=0)
    r2.config(text=answer_choice[indexes[ques]][1], value=1)
    r3.config(text=answer_choice[indexes[ques]][2], value=2)
    r4.config(text=answer_choice[indexes[ques]][3], value=3)
    radiovar.set(user_answers[ques] if user_answers[ques] != -1 else -1)

    update_buttons()
    update_ribbon()
    root.update_idletasks()


def update_nav_button(q):
    """Updates the color of a question button based on its status."""
    if q in marked_questions:
        nav_buttons[q].config(bg="orange")
    elif user_answers[q] != -1:
        nav_buttons[q].config(bg="green")
    elif q in viewed_questions:
        nav_buttons[q].config(bg="red")
    else:
        nav_buttons[q].config(bg="pink")
        
    root.update_idletasks()
 
def update_ribbon():
    """Updates the ribbon counters for Attempted, Marked, and Skipped questions."""
    attempted_count = sum(1 for ans in user_answers if ans != -1)
    marked_count = len(marked_questions)
    skipped_count = sum(1 for i in viewed_questions if user_answers[i] == -1 and i not in marked_questions)

    print(f"DEBUG: Attempted: {attempted_count}, Marked: {marked_count}, Skipped: {skipped_count}")
    
    attempted_label.config(text=f"Attempted: {attempted_count}")
    marked_label.config(text=f"Marked: {marked_count}")
    skipped_label.config(text=f"Skipped: {skipped_count}")

    root.update_idletasks()


def update_buttons():
    """Enables or disables the previous and next buttons appropriately."""
    btnPrev.config(state="normal" if ques > 0 else "disabled")
    btnNext.config(state="disabled" if ques == total_questions - 1 else "normal")


def showresult(score):
    global img_frames, frame_idx, labelimage
    try:
        main_frame.destroy()
    except NameError:
        print("Warning: quiz_frame or nav_grid not found.")

    # Configure root grid for centering
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=3)
    root.grid_columnconfigure(0, weight=1)

    # Student Frame
    student_frame = tk.Frame(root, bg=BG_COLOR2, bd=2, relief="groove")
    student_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
    
    student_frame.grid_columnconfigure(0, weight=1)
    student_name_label = tk.Label(student_frame, text=f"STUDENT: {username}", bg=BG_COLOR2, font=HEADER_MID_FONT, height=2)
    student_name_label.grid(row=0, column=0, padx=15, pady=10, sticky="nsew")
    student_rollno_label = tk.Label(student_frame, text=f"ROLL NO: {rollno}", bg=BG_COLOR2, font=TEXT_SMALL_FONT)
    student_rollno_label.grid(row=1, column=0, padx=15, pady=4, sticky="nsew")
    student_course_label = tk.Label(student_frame, text=f"COURSE: {course}", bg=BG_COLOR2, font=TEXT_SMALL_FONT)
    student_course_label.grid(row=2, column=0, padx=15, pady=4, sticky="nsew")
    student_branch_label = tk.Label(student_frame, text=f"BRANCH: {branch}", bg=BG_COLOR2, font=TEXT_SMALL_FONT)
    student_branch_label.grid(row=3, column=0, padx=15, pady=4, sticky="nsew")

    # Result Frame
    result_frame = tk.Frame(root, bg=BG_COLOR, bd=4, relief="ridge")
    result_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
    result_frame.grid_columnconfigure(0, weight=1)

    # Score and Result Message
    if score / total_questions >= 0.8:
        img_path = "great.gif"
        result_text = "You are Excellent!! 🎉"
    elif score / total_questions >= 0.6:
        img_path = "ok.gif"
        result_text = "You can do better! 😃"
    else:
        img_path = "bad.gif"
        result_text = "Better luck next time! 😢"

    # Load and Resize GIF
    img_frames = []
    gif = Image.open(img_path)
    new_size = (300, 300)
    try:
        while True:
            frame = gif.copy().resize(new_size, Image.Resampling.LANCZOS)
            img_frames.append(ImageTk.PhotoImage(frame))
            gif.seek(len(img_frames))
    except EOFError:
        pass

    # Display GIF
    labelimage = tk.Label(result_frame, background=BG_COLOR)
    labelimage.grid(row=0, column=0, pady=10, sticky="n")

    # GIF Animation
    frame_idx = 0
    def update_gif():
        global frame_idx
        frame_idx = (frame_idx + 1) % len(img_frames)
        labelimage.config(image=img_frames[frame_idx])
        root.after(100, update_gif)
    update_gif()

    # Result Text
    labelresulttext = tk.Label(result_frame, text=result_text, font=HEADER_MID_FONT, bg=BG_COLOR, fg=TEXT_COLOR)
    labelresulttext.grid(row=1, column=0, pady=10, sticky="n")  # Center the text

    # Score Display
    score_label = tk.Label(result_frame, text=f"Your Score: {score}/{total_questions}", 
                           font=TEXT_BIG_FONT, bg=BG_COLOR, fg=HEADER_COLOR, bd=3, relief="solid", padx=10, pady=5)
    score_label.grid(row=2, column=0, pady=10, sticky="n")  # Center the score


def finish_test():
    calc()


def calc():
    """Calculates the score excluding answers marked for review and updates it in the database."""
    score = sum(1 for i in range(total_questions) 
                if i not in marked_questions and user_answers[i] == answers[indexes[i]])
    conn = sqlite3.connect("quiz_results.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE quiz_results SET marks = ? WHERE rollno = ?", (score, rollno))
    conn.commit()
    conn.close()
    showresult(score)


def save_result(name, rollno, course, branch, marks):
    try:
        conn = sqlite3.connect("quiz_results.db")
        c = conn.cursor()
        c.execute("""
            UPDATE quiz_results 
            SET marks = ?
            WHERE rollno = ?
        """, (marks, rollno))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("Error saving result:", e)
        
        
root.mainloop()