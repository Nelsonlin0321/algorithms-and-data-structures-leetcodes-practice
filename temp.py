from hashlib import sha1


def compute_hash(email):
    return sha1(email.encode('utf-8')).hexdigest()


def compute_certificate_id(email):
    email_clean = email.lower().strip()
    return compute_hash(email_clean + '_')


# cohort = 2023
# course = 'mlops-zoomcamp'
your_id = compute_hash('nelsonlin0321@gmail.com')
print(your_id)
# url = f"https://certificate.datatalks.club/{course}/{cohort}/{your_id}.pdf"
# print(url)
