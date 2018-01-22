# Mono Shift - 50pts

In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques.  
  
It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.  

https://ctf.hackerfire.com/resources/introduction-to-ciphers-with-the-caesar-cipher  

Files:  
ciphertext.txt

## Solution
For this challenge the question tells us that in order to get the flag we need to crack some ciphertext that is encrypted using the Caesar Cipher. The author has also given us an explanation of how to encrypt and decrypt using the caesar cipher so I will not be adding more explanations on that front.  
  
The major weakness with the caesar cipher is that the cipher has a really small key space. A key space in cryptography is the set of all possible keys that can be used in the cipher. The more possible keys the better. The keyspace for the classic caesar cipher, however, is only 26 because there are only 26 possible ways to shift the text. This will make cracking the ciphertext by bruteforcing every key very easy.  

To solve this challenge I wrote a simple python script `monoshift_solve.py` that bruteforces every key for me.  
The scripts does the following:  
First is reads in the ciphertext from the file. Next the script runs through a for loop from the numbers 0 to 25. These numbers are going to be our key guesses. The script then decrypts the ciphertext using each key with the following block of code:
```
plain = ""
for char in ciphertext:
    if char.isalpha():
        num = ord(char) - i
        if num < ord('a'):
            num += 26
            plain += chr(num)
        else:
            plain += char
    print plain
```
This code first checks to see if the character is in the alphabet. We do this because some of the ciphertext is not in the alphabet and will not get shifted. Next if the character is the in alphabet we decrypt it with the key we are currently using. In python `ord(char)` returns the decimal representation of that ascii character which allows us to more easily shift the value. If our decrypted character ends up being below the value of `a` we simply add 26 to the value to wrap it back around. Finally the resulting character is appended to the end of the decrypted string using python's `chr(num)` function. This function simply takes a decimal number and returns the corresponding ascii character.  
The output of the script is:  
```
uapv{ndj'kt_qtvjc_ndjg_rgneid_psktcijgth}
tzou{mci'js_psuib_mcif_qfmdhc_orjsbhifsg}
synt{lbh'ir_ortha_lbhe_pelcgb_nqiragherf}
rxms{kag'hq_nqsgz_kagd_odkbfa_mphqzfgdqe}
qwlr{jzf'gp_mprfy_jzfc_ncjaez_logpyefcpd}
pvkq{iye'fo_loqex_iyeb_mbizdy_knfoxdeboc}
oujp{hxd'en_knpdw_hxda_lahycx_jmenwcdanb}
ntio{gwc'dm_jmocv_gwcz_kzgxbw_ildmvbczma}
mshn{fvb'cl_ilnbu_fvby_jyfwav_hkcluabylz}
lrgm{eua'bk_hkmat_euax_ixevzu_gjbktzaxky}
kqfl{dtz'aj_gjlzs_dtzw_hwduyt_fiajsyzwjx}
jpek{csy'zi_fikyr_csyv_gvctxs_ehzirxyviw}
iodj{brx'yh_ehjxq_brxu_fubswr_dgyhqwxuhv}
hnci{aqw'xg_dgiwp_aqwt_etarvq_cfxgpvwtgu}
gmbh{zpv'wf_cfhvo_zpvs_dszqup_bewfouvsft}
flag{you've_begun_your_crypto_adventures}
ekzf{xnt'ud_adftm_xntq_bqxosn_zcudmstqdr}
djye{wms'tc_zcesl_wmsp_apwnrm_ybtclrspcq}
cixd{vlr'sb_ybdrk_vlro_zovmql_xasbkqrobp}
bhwc{ukq'ra_xacqj_ukqn_ynulpk_wzrajpqnao}
agvb{tjp'qz_wzbpi_tjpm_xmtkoj_vyqziopmzn}
zfua{sio'py_vyaoh_siol_wlsjni_uxpyhnolym}
yetz{rhn'ox_uxzng_rhnk_vkrimh_twoxgmnkxl}
xdsy{qgm'nw_twymf_qgmj_ujqhlg_svnwflmjwk}
wcrx{pfl'mv_svxle_pfli_tipgkf_rumveklivj}
vbqw{oek'lu_ruwkd_oekh_shofje_qtludjkhui}
```
To find the flag you just have to manually look through the text and find the correctly decrypted ciphertext which is:  
`flag{you've_begun_your_crypto_adventures}`.


