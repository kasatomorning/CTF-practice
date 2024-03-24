from cryptography import x509
from cryptography.hazmat.backends import default_backend

# 証明書を読み込む
with open("transparency_afff0345c6f99bf80eab5895458d8eab.pem", "rb") as f:
    cert_data = f.read()

# 証明書をパースする
cert = x509.load_pem_x509_certificate(cert_data, default_backend())

# Common Nameを取得する
common_name = cert.subject.get_attributes_for_oid(x509.oid.NameOID.COMMON_NAME)[0].value

# Subject Alternative Nameを取得する
alt_names = cert.extensions.get_extension_for_oid(
    x509.oid.ExtensionOID.SUBJECT_ALTERNATIVE_NAME
)

# ドメイン名を出力する
print(f"Common Name: {common_name}")
for name in alt_names.value:
    print(f"Alternative Name: {name.value}")
