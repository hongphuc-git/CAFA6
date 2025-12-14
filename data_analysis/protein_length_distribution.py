from Bio import SeqIO
import matplotlib.pyplot as plt

fasta_path = "Train/train_sequences.fasta"   # thay thành đường dẫn thật

lengths = []

# Đọc độ dài từng chuỗi
for record in SeqIO.parse(fasta_path, "fasta"):
    lengths.append(len(record.seq))

# Vẽ histogram
plt.figure(figsize=(10,5))
plt.hist(lengths, bins=80)
plt.xlabel("Độ dài chuỗi protein (số amino acid)")
plt.ylabel("Số lượng protein")
plt.title("Phân bố độ dài chuỗi protein trong bộ train")
plt.tight_layout()
plt.show()