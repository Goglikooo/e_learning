# E-Learning Application

Welcome to the E-Learning Application! This application is designed to provide a platform for both students and instructors to engage in online learning activities. The application is built using Django and utilizes SQLite as its database.

## Features

### For Students

1. **View Courses:** Students can explore available courses, read course descriptions, and decide which courses to enroll in.

2. **Enroll in Courses:** Once a student finds a course of interest, they can enroll in it to add it to their schedule.

3. **Mark Courses as Complete:** After completing a course, students have the option to mark it as complete.

4. **View Progress:** Students can view their progress, including the list of enrolled courses and their completion status.

### For Instructors

1. **Add New Courses:** Instructors can add new courses to the platform, providing details such as course name, description, category, and URL.

2. **Create Student Accounts:** Instructors have the ability to create new student accounts, allowing for a seamless onboarding process.

3. **Edit Courses:** Instructors can edit existing courses, modifying details like course name, description, and category.

4. **Delete Courses:** Instructors have the authority to remove courses from the platform.

## Getting Started

Follow these steps to set up and run the E-Learning Application:

1. **Clone the Repository:**
   ```bash
    git clone https://github.com/Goglikooo/e_learning
    cd e_learning
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a Superuser (Instructor):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the Application:**
   ```bash
   python manage.py runserver
   ```

6. **Access the Application:**
   Open your web browser and go to `http://127.0.0.1:8000/`. Log in using the superuser credentials to access instructor functionalities.

## Usage

1. **Students:**
   - Explore courses on the main page.
   - Enroll in a course to add it to your schedule.
   - Mark completed courses as done.
   - View your progress on the progress page.

2. **Instructors:**
   - Log in with superuser credentials.
   - Add new courses on the main page.
   - Create new student accounts.
   - Edit or delete existing courses.
   - Log out when done.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

Thank you for using the E-Learning Application! Happy learning! 📚
