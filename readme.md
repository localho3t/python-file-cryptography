### README for **File Encryptor/Decryptor**

---

## **File Encryptor/Decryptor**
This project provides a simple tool to encrypt and decrypt files using the `cryptography.fernet` library. The encryption key is securely managed in a `.env` file for convenience and enhanced security.

---

### **Features**
- **Automatic Key Generation:** If no encryption key exists, it generates one automatically and stores it in a `.env` file.
- **File Encryption:** Encrypts text or binary files and saves the output with a `.enc` extension.
- **File Decryption:** Decrypts `.enc` files and restores the original content.

---

### **Requirements**
- Python 3.7 or higher
- Dependencies listed in `requirements.txt` (install via `pip install -r requirements.txt`)

---

### **How to Use**

#### 1. Clone the Repository
```bash
git clone <repository_url>
cd <repository_folder>
```

#### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 3. Encrypt a File
```bash
python script.py encrypt <input_file_path> <output_directory>
```
- **Example:**
  ```bash
  python script.py encrypt ./test.txt ./output
  ```

#### 4. Decrypt a File
```bash
python script.py decrypt <encrypted_file_path> <output_directory>
```
- **Example:**
  ```bash
  python script.py decrypt ./output/test.txt.enc ./decrypted
  ```

---

### **Details**

#### **Key Management**
The encryption key is stored in a `.env` file under the variable `ENCRYPTION_KEY`. If the `.env` file does not exist, it is automatically created with a newly generated key.

#### **File Encryption**
- Input files are read in binary mode and encrypted using the `cryptography.fernet` library.
- Encrypted files are saved with the same name as the input file, appended with the `.enc` extension.

#### **File Decryption**
- Encrypted files are read, decrypted, and saved with their original name (by removing the `.enc` extension).

---



### **License**
This project is open-source and licensed under the MIT License.

---

### **Acknowledgments**
Built using the [`cryptography`](https://cryptography.io/en/latest/) library.