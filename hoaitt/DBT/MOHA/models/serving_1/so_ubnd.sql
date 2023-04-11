{{
    config(
        materialized='incremental',
        incremental_strategy='delete+insert'
    )
}}

-- Group code: A026: Số UBND cấp tỉnh
select id, phan_cap, parent_id, ma_dv_hc, ten_dv_hc, ky_du_lieu, thong_tin, param_key, param_value, group_code,
GETDATE() as created_at,
GETDATE() as updated_at,
0 as batch_id,
0 as approve_flag
from {{ref("ubnd")}}
-- filter in incremental models
{% if is_incremental() %}

  -- this filter will only be applied on an incremental run
  where updated_at > (select max(updated_at) from {{ this }})
    -- where label not in (select label from {{ this }})
{% endif %}
