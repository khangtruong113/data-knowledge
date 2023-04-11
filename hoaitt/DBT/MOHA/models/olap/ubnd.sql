{{
    config(
        materialized='incremental',
        unique_key='updated_at',
        incremental_strategy='delete+insert'
    )
}}

-- Group code: A026: Số UBND cấp tỉnh
with A026 as
(
select
    NEWID() id,
    N'Số UBND' thong_tin,
    nk.name ky_du_lieu,
    dvhc.code ma_dv_hc,
    dvhc.name ten_dv_hc,
    '1' phan_cap,
    null parent_id,
    'cap_tinh' param_key,
    fact.so_ubnd_co_ld_chu_chot_nu param_value,
    'A026' group_code,
    GETDATE() created_at,
    GETDATE() updated_at
from {{ source('to_chuc_hanh_chinh', 'f_so_ubnd_co_ld_chu_chot_nu') }} fact
left join {{ source('common', 'd_don_vi_hanh_chinh') }} dvhc on fact.don_vi_hanh_chinh_id = dvhc.id
left join {{ source('to_chuc_hanh_chinh', 'd_nhiem_ky') }} nk on fact.nhiem_ky_id = nk.id
where fact.cap_don_vi_hanh_chinh_id = 2 and tong_so_id is null
),
tong as
(
select
concat_ws(' - ', thong_tin, ky_du_lieu, ten_dv_hc, param_key, group_code) as label,
    *
from A026)
select* from tong
-- filter in incremental models
{% if is_incremental() %}

  -- this filter will only be applied on an incremental run
--   where updated_at > (select max(updated_at) from {{ this }})
    where label not in (select label from {{ this }})
{% endif %}