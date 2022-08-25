from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quiz-app')
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score_label = Label(text=f'Score: 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.q_canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.q_canvas.create_text(
            150,
            125,
            width=280,
            text='Some Question Text',
            fill=THEME_COLOR,
            font=('Arial', 18, 'italic'))
        self.q_canvas.grid(row=1, column=0, columnspan=2, pady=20)

        true_img = PhotoImage(file='images/true.png')
        false_img = PhotoImage(file='images/false.png')
        self.true_button = Button(image=true_img, highlightthickness=0, activebackground=THEME_COLOR,
                                  command=self.true_pressed)
        self.false_button = Button(image=false_img, highlightthickness=0, activebackground=THEME_COLOR,
                                   command=self.false_pressed)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.q_canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.q_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.q_canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.conig(state='disabled')
            self.false_button.config(state='disabled')


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.q_canvas.config(bg='green')
        else:
            self.q_canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
