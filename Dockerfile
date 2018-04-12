FROM python:3.6.5

COPY . /app
WORKDIR /app
RUN pip install             \
    click==6.7              \
    Flask==0.12.2           \
    humanize==0.5.1         \
    itsdangerous==0.24      \
    Jinja2==2.10            \
    MarkupSafe==1.0         \
    Werkzeug==0.14.1
ENV PYTHONPATH=/app ARTIFACTS_PATH=/app/data
EXPOSE 5000
CMD ["python", "src/main.py"]
