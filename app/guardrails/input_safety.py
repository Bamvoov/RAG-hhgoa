UNSAFE={'bomb','terrorist','kill','suicide'}
def check_input_safety(text):
    bad=UNSAFE & set(text.lower().split()); return {'name':'input_safety','allowed':not bad,'reason':'unsafe terms: '+', '.join(sorted(bad)) if bad else 'passed'}
