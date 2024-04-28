# Corporate Assets Tracking

This Django application is designed to track corporate assets such as phones, tablets, laptops, and other gears handed out to employees.

## Overview

The application allows multiple companies to manage their assets and employees. Each company can delegate devices to employees for a specified period, track when a device was checked out and returned, and maintain a log of the device condition at checkout and return.

## Features

- **Company Management:** Add, update, or delete company details.
- **Employee Management:** Manage employees under each company.
- **Device Management:** Add various types of devices and track their condition.
- **Device Log:** Log the condition of devices when checked out and returned by employees.

## Tech Stack

- Django
- Django REST Framework

## Project Structure

```
corporate_assets_tracking/
├── corporate_assets_tracking/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── assets/
│ ├── migrations/
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── tests.py
│ └── views.py
└── manage.py
```



## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/schnehowebking/corporate_assets_tracking_django_drf.git
    ```

2. Navigate to the project directory:

    ```bash
    cd corporate-assets-tracking
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the migrations:

    ```bash
    python manage.py migrate
    ```

5. Start the development server:

    ```bash
    python manage.py runserver
    ```

## API Endpoints

- **Companies:** `/companies/`
- **Employees:** `/employees/`
- **Devices:** `/devices/`
- **Device Logs:** `/device-logs/`

## Contributing

We welcome contributions! Please feel free to fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
