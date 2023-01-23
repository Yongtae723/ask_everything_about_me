format:
	black .
	isort .

startup_app:
	pip install poetry
	poetry install
	poetry run streamlit run app.py