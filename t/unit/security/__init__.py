"""
Keys and certificates for tests (KEY1 is a private key of CERT1, etc.)

Generated with `extra/security/get-cert.sh`
"""

KEYPASSWORD = b"samplepassword"

KEY1 = """-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQC9Twh0V5q/R1Q8N+Y+CNM4lj9AXeZL0gYowoK1ht2ZLCDU9vN5
dhV0x3sqaXLjQNeCGd6b2vTbFGdF2E45//IWz6/BdPFWaPm0rtYbcxZHqXDZScRp
vFDLHhMysdqQWHxXVxpqIXXo4B7bnfnGvXhYwYITeEyQylV/rnH53mdV8wIDAQAB
AoGBAKUJN4elr+S9nHP7D6BZNTsJ0Q6eTd0ftfrmx+jVMG8Oh3jh6ZSkG0R5e6iX
0W7I4pgrUWRyWDB98yJy1o+90CAN/D80o8SbmW/zfA2WLBteOujMfCEjNrc/Nodf
6MZ0QQ6PnPH6pp94i3kNmFD8Mlzm+ODrUjPF0dCNf474qeKhAkEA7SXj5cQPyQXM
s15oGX5eb6VOk96eAPtEC72cLSh6o+VYmXyGroV1A2JPm6IzH87mTqjWXG229hjt
XVvDbdY2uQJBAMxblWFaWJhhU6Y1euazaBl/OyLYlqNz4LZ0RzCulEoV/gMGYU32
PbilD5fpFsyhp5oCxnWNEsUFovYMKjKM3AsCQQCIlOcBoP76ZxWzRK8t56MaKBnu
fiuAIzbYkDbPp12i4Wc61wZ2ozR2Y3u4Bh3tturb6M+04hea+1ZSC5StwM85AkAp
UPLYpe13kWXaGsHoVqlbTk/kcamzDkCGYufpvcIZYGzkq6uMmZZM+II4klWbtasv
BhSdu5Hp54PU/wyg/72VAkBy1/oM3/QJ35Vb6TByHBLFR4nOuORoRclmxcoCPva9
xqkQQn+UgBtOemRXpFCuKaoXonA3nLeB54SWcC6YUOcR
-----END RSA PRIVATE KEY-----"""

ENCKEY1 = """-----BEGIN ENCRYPTED PRIVATE KEY-----
MIIC3TBXBgkqhkiG9w0BBQ0wSjApBgkqhkiG9w0BBQwwHAQIfSuXbPVZsP8CAggA
MAwGCCqGSIb3DQIJBQAwHQYJYIZIAWUDBAEqBBBP/mVP1cCpfTpoJZuSKRrnBIIC
gMKyrj4mzdr0xASR4120M3mh56+1dUDvLJl0DwOXD5NGCQfvSgDP0mGSrmIcM6Rh
O9oePFj81IjHoGQNVgFNhd8Lc1R7xe51Vk8M3VfCOnPwWzuBzGe8vlgyfzKRVhgo
vb633pZR721xcPCK08aEXcsLwXrMGpp/EtHtpJD7MwqVFOhUjcUhKWNa7icFkVR1
fzL6CC24CjsJWFz8esdJUNwGJv2vcYcoYYcIkVX5s1riSemhUmPCVTvT1Rvl2yTE
T2oHWCCMD5lhd+gcsSlcK/PlUY9J5GMJd61w+uD2A5qVOzOHDIRIwjRUbGpS2feL
1rWUjBbF8YF8mUp1cYdJSjKE9ro2qZbbFRLB+il3FLimjb1yFEAEItQzR123loJ6
cTrQEg9WZmLTwrxsOx54bYR6CGBU1fpVkpeR95xYtKyhfK1RD03Aj6ffcDiaJH73
lodf+ObBORYMYBi6E0AJvv2HNJHaZVzmj+ynzeTV6rfUyP075YZjS5XoRYKCOQz6
HcssJUeGT+voPTbf67AO/clJDgOBn82fa8eIMGibgQARtOcEuhac9Gl4R2whfbdp
DkODqVKiqHCgO5qxGxmE/cEZpa7+j6Q8YTVWlvGdDtBQK4+NB1hHgnsPsG9RLjWy
Z7Ch/UjkmMxNGnvwWb9Xaq56ZqOmQGmoet+v9OLXAKZwZMRaURuJffxbd+YrexnE
LF9xV1b+w1taLrGCNn8yLDJY9G/T9zsH6eGjZslT9MPLlxq4PaL7WysKGhOt2+Vw
beQ4tDVmjlJjODOyaygt0wwzEght02lZmGhL88S35hfWpyskcWzGfbYkGqJVxY5E
i8wow1MqvPUQdKWNPgPGd04=
-----END ENCRYPTED PRIVATE KEY-----"""

KEY2 = """-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQDH22L8b9AmST9ABDmQTQ2DWMdDmK5YXZt4AIY81IcsTQ/ccM0C
fwXEP9tdkYwtcxMCWdASwY5pfMy9vFp0hyrRQMSNfuoxAgONuNWPyQoIvY3ZXRe6
rS+hb/LN4+vdjX+oxmYiQ2HmSB9rh2bepE6Cw+RLJr5sXXq+xZJ+BLt5tQIDAQAB
AoGBAMGBO0Arip/nP6Rd8tYypKjN5nEefX/1cjgoWdC//fj4zCil1vlZv12abm0U
JWNEDd2y0/G1Eow0V5BFtFcrIFowU44LZEiSf7sKXlNHRHlbZmDgNXFZOt7nVbHn
6SN+oCYjaPjji8idYeb3VQXPtqMoMn73MuyxD3k3tWmVLonpAkEA6hsu62qhUk5k
Nt88UZOauU1YizxsWvT0bHioaceE4TEsbO3NZs7dmdJIcRFcU787lANaaIq7Rw26
qcumME9XhwJBANqMOzsYQ6BX54UzS6x99Jjlq9MEbTCbAEZr/yjopb9f617SwfuE
AEKnIq3HL6/Tnhv3V8Zy3wYHgDoGNeTVe+MCQQDi/nyeNAQ8RFqTgh2Ak/jAmCi0
yV/fSgj+bHgQKS/FEuMas/IoL4lbrzQivkyhv5lLSX0ORQaWPM+z+A0qZqRdAkBh
XE+Wx/x4ljCh+nQf6AzrgIXHgBVUrfi1Zq9Jfjs4wnaMy793WRr0lpiwaigoYFHz
i4Ei+1G30eeh8dpYk3KZAkB0ucTOsQynDlL5rLGYZ+IcfSfH3w2l5EszY47kKQG9
Fxeq/HOp9JYw4gRu6Ycvqu57KHwpHhR0FCXRBxuYcJ5V
-----END RSA PRIVATE KEY-----"""

ENCKEY2 = """-----BEGIN ENCRYPTED PRIVATE KEY-----
MIIC3TBXBgkqhkiG9w0BBQ0wSjApBgkqhkiG9w0BBQwwHAQIbWgdUR8UE/cCAggA
MAwGCCqGSIb3DQIJBQAwHQYJYIZIAWUDBAEqBBA50e1NvEUQXLkA44V4wVeOBIIC
gBt+cRTT+Jqrayj1hSrKgD20mNKz0qo6/JsXwTcHQJLQ91KFWDkAfCYOazzzIlIx
/rsJqz6IY1LckwL2Rtls3hp4+tNPD4AregtadMKgJj5lOyX1RYGdbkjTkhymMKKo
3f5sayoIXkOovT9qADKGjVaHL2tmc5hYJhtNHGKiy+CqraN+h8fOsZsSJDLoWCZV
iSC2rXBsWvqq0ItBEeJhvoCqzOg+ZL7SNrHez6/g8de8xob9eLXZMw6CWiZJ6NJa
mcBMIw+ep6nfZ53rQd/5N5T5B4b0EYK+DM8eypqljbc81IvKvPc3HsoU/TFC+3XW
2qoaQVbsZu8kOyY7xqR/MO3H2klRAVIEBgzqU/ZGl0abLyn7PcV4et8ld8zfwR1c
0Whpq+9kN5O1RWIKU/CU4Xx2WwBLklnqV9U8rHF6FGcSi62rCzkv6GhHpoO6wi3w
vP08ACHMa4of/WJhqKmBic9Q3IMf77irJRS7cqkwkjr7mIzazQvouQCHma5y5moQ
x1XfkX3U7qZwdCOtDcfFVLfeWnY7iEbeoMKJu/siJAkbWI45jRLANQMn6Y4nu3oS
S+XeYxmDBV0JJEBkaTuck9rb0X9TU+Ms6pGvTXTt4r2jz+GUVuFDHCp3MlRD64tb
d1VBresyllIFF39adeKyVeW+pp3q1fd2N7pNKo+oDiIg+rDwNtvA9sX10j6gh8Wp
LZZYJpiMpmof/eMMm6LTgjoJ+PZHRGtR1B8VF5RtuNioDWvpQAvnJS5cG1IjD7Sq
Q0EqU7r50YZJbDqA67dpHeC4iDxYoANbX8BP5E9fD1yEQGkEXmsogj5SokjqR2ef
iXQ8ER5I8IKAr2KjDXTJyZg=
-----END ENCRYPTED PRIVATE KEY-----"""

CERT1 = """-----BEGIN CERTIFICATE-----
MIICVzCCAcACCQC72PP7b7H9BTANBgkqhkiG9w0BAQUFADBwMQswCQYDVQQGEwJV
UzELMAkGA1UECBMCQ0ExCzAJBgNVBAcTAlNGMQ8wDQYDVQQKEwZDZWxlcnkxDzAN
BgNVBAMTBkNFbGVyeTElMCMGCSqGSIb3DQEJARYWY2VydEBjZWxlcnlwcm9qZWN0
Lm9yZzAeFw0xMzA3MjQxMjExMTRaFw0xNDA3MjQxMjExMTRaMHAxCzAJBgNVBAYT
AlVTMQswCQYDVQQIEwJDQTELMAkGA1UEBxMCU0YxDzANBgNVBAoTBkNlbGVyeTEP
MA0GA1UEAxMGQ0VsZXJ5MSUwIwYJKoZIhvcNAQkBFhZjZXJ0QGNlbGVyeXByb2pl
Y3Qub3JnMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC9Twh0V5q/R1Q8N+Y+
CNM4lj9AXeZL0gYowoK1ht2ZLCDU9vN5dhV0x3sqaXLjQNeCGd6b2vTbFGdF2E45
//IWz6/BdPFWaPm0rtYbcxZHqXDZScRpvFDLHhMysdqQWHxXVxpqIXXo4B7bnfnG
vXhYwYITeEyQylV/rnH53mdV8wIDAQABMA0GCSqGSIb3DQEBBQUAA4GBAKA4tD3J
94tsnQxFxHP7Frt7IvGMH+3wMqOiXFgYxPJX2tyaPvOLJ/7ERE4MkrvZO7IRC0iA
yKBe0pucdrTgsJoDV8juahuyjXOjvU14+q7Wv7pj7zqddVavzK8STLX4/FMIDnbK
aMGJl7wyj6V2yy6ANSbmy0uQjHikI6DrZEoK
-----END CERTIFICATE-----"""

CERT2 = """-----BEGIN CERTIFICATE-----
MIICATCCAWoCCQCV/9A2ZBM37TANBgkqhkiG9w0BAQUFADBFMQswCQYDVQQGEwJB
VTETMBEGA1UECAwKU29tZS1TdGF0ZTEhMB8GA1UECgwYSW50ZXJuZXQgV2lkZ2l0
cyBQdHkgTHRkMB4XDTExMDcxOTA5MDkwMloXDTEyMDcxODA5MDkwMlowRTELMAkG
A1UEBhMCQVUxEzARBgNVBAgMClNvbWUtU3RhdGUxITAfBgNVBAoMGEludGVybmV0
IFdpZGdpdHMgUHR5IEx0ZDCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEAx9ti
/G/QJkk/QAQ5kE0Ng1jHQ5iuWF2beACGPNSHLE0P3HDNAn8FxD/bXZGMLXMTAlnQ
EsGOaXzMvbxadIcq0UDEjX7qMQIDjbjVj8kKCL2N2V0Xuq0voW/yzePr3Y1/qMZm
IkNh5kgfa4dm3qROgsPkSya+bF16vsWSfgS7ebUCAwEAATANBgkqhkiG9w0BAQUF
AAOBgQBzaZ5vBkzksPhnWb2oobuy6Ne/LMEtdQ//qeVY4sKl2tOJUCSdWRen9fqP
e+zYdEdkFCd8rp568Eiwkq/553uy4rlE927/AEqs/+KGYmAtibk/9vmi+/+iZXyS
WWZybzzDZFncq1/N1C3Y/hrCBNDFO4TsnTLAhWtZ4c0vDAiacw==
-----END CERTIFICATE-----"""

CERT_ECDSA = """-----BEGIN CERTIFICATE-----
MIIDTTCCATWgAwIBAgIBCTANBgkqhkiG9w0BAQsFADANMQswCQYDVQQGEwJGSTAe
Fw0yMjA4MDQwOTA5MDlaFw0yNTA0MzAwOTA5MDlaMCMxCzAJBgNVBAYTAkZJMRQw
EgYDVQQDDAtUZXN0IFNlcnZlcjBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABIZV
GFM0uPbXehT55s2yq3Zd7tCvN6GMGpE2+KSZqTtDP5c7x23QvBYF6q/T8MLNWCSB
TxaERpvt8XL+ksOZ8vSjbTBrMB0GA1UdDgQWBBRiY7qDBo7KAYJIn3qTMGAkPimO
6TAyBgNVHSMEKzApoRGkDzANMQswCQYDVQQGEwJGSYIUN/TljutVzZQ8GAMSX8yl
Fy9dO/8wCQYDVR0TBAIwADALBgNVHQ8EBAMCBaAwDQYJKoZIhvcNAQELBQADggIB
AKADv8zZvq8TWtvEZSmf476u+sdxs1hROqqSSJ0M3ePJq2lJ+MGI60eeU/0AyDRt
Q5XAjr2g9wGY3sbA9uYmsIc2kaF+urrUbeoGB1JstALoxviGuM0EzEf+wK5/EbyA
DDMg9j7b51CBMb3FjkiUQgOjM/u5neYpFxF0awXm4khThdOKTFd0FLVX+mcaKPZ4
dkLcM/0NL25896DBPN982ObHOVqQjtY3sunXVuyeky8rhKmDvpasYu9xRkzSJBp7
sCPnY6nsCexVICbuI+Q9oNT98YjHipDHQU0U/k/MvK7K/UCY2esKAnxzcOqoMQhi
UjsKddXQ29GUEA9Btn9QB1sp39cR75S8/mFN2f2k/LhNm8j6QeHB4MhZ5L2H68f3
K2wjzQHMZUrKXf3UM00VbT8E9j0FQ7qjYa7ZnQScvhTqsak2e0um8tqcPyk4WD6l
/gRrLpk8l4x/Qg6F16hdj1p5xOsCUcVDkhIdKf8q3ZXjU2OECYPCFVOwiDQ2ngTf
Se/bcjxgYXBQ99rkEf0vxk47KqC2ZBJy5enUxqUeVbbqho46vJagMzJoAmzp7yFP
c1g8aazOWLD2kUxcqkUn8nv2HqApfycddz2O7OJ5Hl8e4vf+nVliuauGzImo0fiK
VOL9+/r5Kek0fATRWdL4xtbB7zlk+EuoP9T5ZoTYlf14
-----END CERTIFICATE-----"""

KEY_ECDSA = """-----BEGIN EC PARAMETERS-----
BggqhkjOPQMBBw==
-----END EC PARAMETERS-----
-----BEGIN EC PRIVATE KEY-----
MHcCAQEEIOj98rAhc4ToQkHby+Iegvhm3UBx+3TwpfNza+2Vn8d7oAoGCCqGSM49
AwEHoUQDQgAEhlUYUzS49td6FPnmzbKrdl3u0K83oYwakTb4pJmpO0M/lzvHbdC8
FgXqr9Pwws1YJIFPFoRGm+3xcv6Sw5ny9A==
-----END EC PRIVATE KEY-----"""
