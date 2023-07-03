{% macro limit_data_in_dev(column_name, dev_days_of_data = 3) %}
{% if target_name == 'dev' %}
where {{ column_name }} >= DATEADD('day', - {{ dev_days_of_data }}, CURRENT_TIMESTAMP)
{% endif %}
{% endmacro %}