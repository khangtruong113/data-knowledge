{% test compare_models(model, column_name, field, to) %}
-- Compare view has created from transformation to relative table in serving_1 database

select s.*
from {{ model }} s
left join {{ to }} t
on s.{{column_name}} = t.{{field}} and s.group_code = t.group_code and s.ky_du_lieu = t.ky_du_lieu and s.ma_dv_hc = t.ma_dv_hc
where s.param_value != t.param_value

{% endtest %}
