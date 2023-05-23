select t1.group_code, t1.ky_du_lieu, t1.ma_dv_hc
from {{ref('ubnd')}} t1
left join {{source('linh_vuc_01','so_ubnd')}} t2 on t1.group_code = t2.group_code and t1. ma_dv_hc = t2.ma_dv_hc and t1.ky_du_lieu = t2.ky_du_lieu
where t1.param_value != t2.param_value