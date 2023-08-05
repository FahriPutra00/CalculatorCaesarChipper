import streamlit as st

class CaesarCipher:
    # Membuat fungsi enkripsi dan dekripsi
    @staticmethod
    def encrypt(plaintext, key):
        ciphertext = ""
        for huruf in plaintext:
            if huruf.isalpha(): #Mengecek apakah huruf atau bukan
                #Mengecek apakah huruf besar atau kecil
                start_ascii = 65 if huruf.isupper() else 97 #Huruf Besar = 65, huruf kecil = 97
                #Mencari nilai ASCII dari huruf Besar/huruf kecil
                ciphertext += chr((ord(huruf) - start_ascii + key) % 26 + start_ascii) #65 adalah nilai ASCII dari huruf A, 97 adalah nilai ASCII dari huruf a0
            else:
                ciphertext += huruf
        return ciphertext

    @staticmethod
    def decrypt(ciphertext, key):
        plaintext = ""
        for huruf in ciphertext:
            if huruf.isalpha():
                start_ascii = 65 if huruf.isupper() else 97
                plaintext += chr((ord(huruf) - start_ascii - key) % 26 + start_ascii)
            else:
                plaintext += huruf
        return plaintext

# Membuat Tampilan Streamlit
def app():
    st.title("Kalkulator Caesar Cipher")
    st.write("Kalkulator ini digunakan untuk mengenkripsi dan mendekripsi pesan menggunakan metode Caesar Cipher\n")
    st.write("5200411389 Fahri Putra Herlambang\n")
    
    plaintext = st.text_input("Enter plaintext (Contoh : Fahri Putra Herlambang)")
    key = st.number_input("Enter key:", min_value=0, max_value=25, value=1)
    ciphertext = st.text_input("Enter ciphertext (Contoh : Xyphr Xxiy)")
    if st.button("Enkripsi"):
        ciphertext = CaesarCipher.encrypt(plaintext, key) #Menggunakan fungsi enkripsi
        st.text_input(f"Hasil Enkripsi kata = {plaintext} , k = {key}", value=ciphertext)
    
    if st.button("Deskripsi"):
        plaintext = CaesarCipher.decrypt(ciphertext, key) #Menggunakan fungsi dekripsi
        st.text_input(f"Hasil Enkripsi kata = {ciphertext} , k = {key}", value=plaintext) 


# Run the app
if __name__ == "__main__":
    app()
