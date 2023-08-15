#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def rpm_calcs(P,L,H,lnc_arr,ldc_arr,snc_arr,sdc_arr):
        
        sum_lnc=         (lnc_arr[0]) + (lnc_arr[1] * L) + (lnc_arr[2] * P) + (lnc_arr[3] * H) + (lnc_arr[4] * L * P) +         (lnc_arr[5] * L * H) + (lnc_arr[6] * P * H) + (lnc_arr[7] * L**2) + (lnc_arr[8] * P**2) + (lnc_arr[9] * H**2) +         (lnc_arr[10] * P * L * H) + (lnc_arr[11] * L**3) + (lnc_arr[12] * L * P**2) + (lnc_arr[13] * L * H**2) + (lnc_arr[14] * L**2 * P) +         (lnc_arr[15] * P**3) + (lnc_arr[16] * P * H**2) + (lnc_arr[17] * L**2 * H) + (lnc_arr[18] * P**2 * H) + (lnc_arr[19] * H**3)

        sum_ldc=         (ldc_arr[0]) + (ldc_arr[1] * L) + (ldc_arr[2] * P) + (ldc_arr[3] * H) + (ldc_arr[4] * L * P) +         (ldc_arr[5] * L * H) + (ldc_arr[6] * P * H) + (ldc_arr[7] * L**2) + (ldc_arr[8] * P**2) + (ldc_arr[9] * H**2) +         (ldc_arr[10] * P * L * H) + (ldc_arr[11] * L**3) + (ldc_arr[12] * L * P**2) + (ldc_arr[13] * L * H**2) + (ldc_arr[14] * L**2 * P) +         (ldc_arr[15] * P**3) + (ldc_arr[16] * P * H**2) + (ldc_arr[17] * L**2 * H) + (ldc_arr[18] * P**2 * H) + (ldc_arr[19] * H**3)

        sum_snc=         (snc_arr[0]) + (snc_arr[1] * L) + (snc_arr[2] * P) + (snc_arr[3] * H) + (snc_arr[4] * L * P) +         (snc_arr[5] * L * H) + (snc_arr[6] * P * H) + (snc_arr[7] * L**2) + (snc_arr[8] * P**2) + (snc_arr[9] * H**2) +         (snc_arr[10] * P * L * H) + (snc_arr[11] * L**3) + (snc_arr[12] * L * P**2) + (snc_arr[13] * L * H**2) + (snc_arr[14] * L**2 * P) +         (snc_arr[15] * P**3) + (snc_arr[16] * P * H**2) + (snc_arr[17] * L**2 * H) + (snc_arr[18] * P**2 * H) + (snc_arr[19] * H**3)

        sum_sdc=         (sdc_arr[0]) + (sdc_arr[1] * L) + (sdc_arr[2] * P) + (sdc_arr[3] * H) + (sdc_arr[4] * L * P) +         (sdc_arr[5] * L * H) + (sdc_arr[6] * P * H) + (sdc_arr[7] * L**2) + (sdc_arr[8] * P**2) + (sdc_arr[9] * H**2) +         (sdc_arr[10] * P * L * H) + (sdc_arr[11] * L**3) + (sdc_arr[12] * L * P**2) + (sdc_arr[13] * L * H**2) + (sdc_arr[14] * L**2 * P) +         (sdc_arr[15] * P**3) + (sdc_arr[16] * P * H**2) + (sdc_arr[17] * L**2 * H) + (sdc_arr[18] * P**2 * H) + (sdc_arr[19] * H**3)

        rn=sum_lnc/sum_ldc
        cn=sum_snc/sum_sdc
        
        return rn,cn

