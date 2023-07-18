{% macro dollars_to_cents(column_name, scale=2) %}
    ({{ column_name }} * 100)
{% endmacro %}
