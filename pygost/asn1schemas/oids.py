from pyderasn import ObjectIdentifier


id_at_commonName = ObjectIdentifier("2.5.4.3")
id_at_countryName = ObjectIdentifier("2.5.4.6")
id_at_localityName = ObjectIdentifier("2.5.4.7")
id_at_stateOrProvinceName = ObjectIdentifier("2.5.4.8")
id_at_organizationName = ObjectIdentifier("2.5.4.10")

id_pkcs7 = ObjectIdentifier("1.2.840.113549.1.7")
id_data = id_pkcs7 + (1,)
id_signedData = id_pkcs7 + (2,)
id_envelopedData = id_pkcs7 + (3,)
id_digestedData = id_pkcs7 + (5,)
id_encryptedData = id_pkcs7 + (6,)

id_pkcs9 = ObjectIdentifier("1.2.840.113549.1.9")
id_contentType = id_pkcs9 + (3,)
id_messageDigest = id_pkcs9 + (4,)
id_pkcs9_certTypes_x509Certificate = ObjectIdentifier("1.2.840.113549.1.9.22.1")
id_pkcs12_bagtypes_keyBag = ObjectIdentifier("1.2.840.113549.1.12.10.1.1")
id_pkcs12_bagtypes_pkcs8ShroudedKeyBag = ObjectIdentifier("1.2.840.113549.1.12.10.1.2")
id_pkcs12_bagtypes_certBag = ObjectIdentifier("1.2.840.113549.1.12.10.1.3")

id_Gost28147_89 = ObjectIdentifier("1.2.643.2.2.21")
id_GostR3410_2001_TestParamSet = ObjectIdentifier("1.2.643.2.2.35.0")
id_cms_mac_attr = ObjectIdentifier("1.2.643.7.1.0.6.1.1")
id_tc26_gost3410_2012_256 = ObjectIdentifier("1.2.643.7.1.1.1.1")
id_tc26_gost3410_2012_512 = ObjectIdentifier("1.2.643.7.1.1.1.2")
id_tc26_gost3411_2012_256 = ObjectIdentifier("1.2.643.7.1.1.2.2")
id_tc26_gost3411_2012_512 = ObjectIdentifier("1.2.643.7.1.1.2.3")
id_tc26_signwithdigest_gost3410_2012_256 = ObjectIdentifier("1.2.643.7.1.1.3.2")
id_tc26_signwithdigest_gost3410_2012_512 = ObjectIdentifier("1.2.643.7.1.1.3.3")
id_gostr3412_2015_magma_ctracpkm = ObjectIdentifier("1.2.643.7.1.1.5.1.1")
id_gostr3412_2015_magma_ctracpkm_omac = ObjectIdentifier("1.2.643.7.1.1.5.1.2")
id_gostr3412_2015_kuznyechik_ctracpkm = ObjectIdentifier("1.2.643.7.1.1.5.2.1")
id_gostr3412_2015_kuznyechik_ctracpkm_omac = ObjectIdentifier("1.2.643.7.1.1.5.2.2")
id_tc26_agreement_gost3410_2012_256 = ObjectIdentifier("1.2.643.7.1.1.6.1")
id_tc26_agreement_gost3410_2012_512 = ObjectIdentifier("1.2.643.7.1.1.6.2")
id_gostr3412_2015_magma_wrap_kexp15 = ObjectIdentifier("1.2.643.7.1.1.7.1.1")
id_gostr3412_2015_kuznyechik_wrap_kexp15 = ObjectIdentifier("1.2.643.7.1.1.7.2.1")
id_tc26_gost3410_2012_256_paramSetA = ObjectIdentifier("1.2.643.7.1.2.1.1.1")
id_tc26_gost3410_2012_256_paramSetB = ObjectIdentifier("1.2.643.7.1.2.1.1.2")
id_tc26_gost3410_2012_256_paramSetC = ObjectIdentifier("1.2.643.7.1.2.1.1.3")
id_tc26_gost3410_2012_256_paramSetD = ObjectIdentifier("1.2.643.7.1.2.1.1.4")
id_tc26_gost3410_2012_512_paramSetTest = ObjectIdentifier("1.2.643.7.1.2.1.2.0")
id_tc26_gost3410_2012_512_paramSetA = ObjectIdentifier("1.2.643.7.1.2.1.2.1")
id_tc26_gost3410_2012_512_paramSetB = ObjectIdentifier("1.2.643.7.1.2.1.2.2")
id_tc26_gost3410_2012_512_paramSetC = ObjectIdentifier("1.2.643.7.1.2.1.2.3")
id_tc26_gost_28147_param_Z = ObjectIdentifier("1.2.643.7.1.2.5.1.1")

id_pbes2 = ObjectIdentifier("1.2.840.113549.1.5.13")
id_pbkdf2 = ObjectIdentifier("1.2.840.113549.1.5.12")

id_at_commonName = ObjectIdentifier("2.5.4.3")
id_ce_basicConstraints = ObjectIdentifier("2.5.29.19")
id_ce_subjectKeyIdentifier = ObjectIdentifier("2.5.29.14")
id_ce_keyUsage = ObjectIdentifier("2.5.29.15")
id_ce_subjectAltName = ObjectIdentifier("2.5.29.17")
id_ce_authorityKeyIdentifier = ObjectIdentifier("2.5.29.35")