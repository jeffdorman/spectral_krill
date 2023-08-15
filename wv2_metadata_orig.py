#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def extract_RPC_data(root):
    
    import xml.etree.cElementTree as et
    import numpy as np
    
    
    lat_off=[]
    lon_off=[]
    lat_sc=[]
    lon_sc=[]
    h_off=[]
    h_sc=[]
    line_off=[]
    line_sc=[]
    samp_off=[]
    samp_sc=[]
    lnc=[]
    ldc=[]
    snc=[]
    sdc=[]

    for LAT_OFF in root.iter('LATOFFSET'):
        lat_off.append(LAT_OFF.text)
    lat_off=float(lat_off[0])

    for LAT_SC in root.iter('LATSCALE'):
        lat_sc.append(LAT_SC.text)
    lat_sc=float(lat_sc[0])

    for LON_OFF in root.iter('LONGOFFSET'):
        lon_off.append(LON_OFF.text)
    lon_off=float(lon_off[0])

    for LON_SC in root.iter('LONGSCALE'):
        lon_sc.append(LON_SC.text)
    lon_sc=float(lon_sc[0])

    for H_OFF in root.iter('HEIGHTOFFSET'):
        h_off.append(H_OFF.text)
    h_off=float(h_off[0])

    for H_SC in root.iter('HEIGHTSCALE'):
        h_sc.append(H_SC.text)
    h_sc=float(h_sc[0])

    for LINE_OFF in root.iter('LINEOFFSET'):
        line_off.append(LINE_OFF.text)
    line_off=float(line_off[0])

    for LINE_SC in root.iter('LINESCALE'):
        line_sc.append(LINE_SC.text)
    line_sc=float(line_sc[0])

    for SAMP_OFF in root.iter('SAMPOFFSET'):
        samp_off.append(SAMP_OFF.text)
    samp_off=float(samp_off[0])

    for SAMP_SC in root.iter('SAMPSCALE'):
        samp_sc.append(SAMP_SC.text)
    samp_sc=float(samp_sc[0])

    for LNC in root.iter('LINENUMCOEF'):
        lnc.append(LNC.text)

    for LDC in root.iter('LINEDENCOEF'):
        ldc.append(LDC.text)

    for SNC in root.iter('SAMPNUMCOEF'):
        snc.append(SNC.text)

    for SDC in root.iter('SAMPDENCOEF'):
        sdc.append(SDC.text)
        
    lnc_arr=np.empty([20], dtype=float)
    ldc_arr=np.empty([20], dtype=float)
    snc_arr=np.empty([20], dtype=float)
    sdc_arr=np.empty([20], dtype=float)

    lnc_strarray=np.array(lnc[0].split(' '))
    for ii in range(0,len(lnc_strarray)):
        lnc_arr[ii]=float(lnc_strarray[ii])

    ldc_strarray=np.array(ldc[0].split(' '))
    for ii in range(0,len(ldc_strarray)):
        ldc_arr[ii]=float(ldc_strarray[ii])

    snc_strarray=np.array(snc[0].split(' '))
    for ii in range(0,len(snc_strarray)):
        snc_arr[ii]=float(snc_strarray[ii])

    sdc_strarray=np.array(sdc[0].split(' '))
    for ii in range(0,len(sdc_strarray)):
        sdc_arr[ii]=float(sdc_strarray[ii])
        
    return lat_off, lon_off, lat_sc, lon_sc, h_off, h_sc,            line_off, line_sc, samp_off, samp_sc,            lnc_arr, ldc_arr, snc_arr, sdc_arr

def extract_conversion_params(root):
    
    import xml.etree.cElementTree as et
    import numpy as np
    from datetime import datetime, time

    ACF=[]
    EBW=[]
    MSE=[]
    tlctime=[]
    for acf in root.iter('ABSCALFACTOR'):
        ACF.append(acf.text)
    b1_acf=float(ACF[0])
    b2_acf=float(ACF[1])
    b3_acf=float(ACF[2])
    b4_acf=float(ACF[3])
    b5_acf=float(ACF[4])
    b6_acf=float(ACF[5])
    b7_acf=float(ACF[6])
    b8_acf=float(ACF[7])

    for ebw in root.iter('EFFECTIVEBANDWIDTH'):
        EBW.append(ebw.text)
    b1_ebw=float(EBW[0])
    b2_ebw=float(EBW[1])
    b3_ebw=float(EBW[2])
    b4_ebw=float(EBW[3])
    b5_ebw=float(EBW[4])
    b6_ebw=float(EBW[5])
    b7_ebw=float(EBW[6])
    b8_ebw=float(EBW[7])

    for mse in root.iter('MEANSUNEL'):
        MSE.append(float(mse.text))

    for tlc in root.iter('TLCTIME'):
        tlctime.append(tlc.text)
    datetime_str = tlctime[0]
    datetime_str=datetime_str[0:10]
    datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d')#T%H:%M:%S')
    year_day = datetime_object.timetuple().tm_yday
    #from https://physics.stackexchange.com/questions/177949/earth-sun-distance-on-a-given-day-of-the-year
    #Earth/Sun Distance
    #dES=1-0.01672*np.cos(0.9856*(yd-4))
    dES=1-(0.01672*np.cos(np.radians(0.9856*(year_day-4))))
    
    return b1_acf, b2_acf, b3_acf, b4_acf, b5_acf, b6_acf, b7_acf, b8_acf,            b2_ebw, b2_ebw, b3_ebw, b4_ebw, b5_ebw, b6_ebw, b7_ebw, b8_ebw,            MSE, dES

