import heapq

class EmergencyQueue:
    def __init__(self):
        self.queue = []  # Inisialisasi heap kosong

    def add_patient(self, name, priority):
        heapq.heappush(self.queue, (priority, name))  # Tambah pasien ke heap
    
    def process_patient(self):
        if not self.is_empty():
            return heapq.heappop(self.queue)[1]  # Ambil pasien dengan prioritas tertinggi
        else:
            return "Antrian kosong!"

    def display_queue(self):
        sorted_queue = sorted(self.queue)  # Urutkan berdasarkan prioritas
        print([patient[1] for patient in sorted_queue])  # Cetak nama pasien

    def is_empty(self):
        return len(self.queue) == 0

if __name__ == "__main__":
    queue = EmergencyQueue()

    # Tambah pasien dengan berbagai prioritas
    queue.add_patient("Krisna", 2)  
    queue.add_patient("Surya", 1)  
    queue.add_patient("Jon", 3)  
    queue.add_patient("Idris", 1)  

    # Tampilkan antrian
    print("Antrian saat ini:")
    queue.display_queue()  

    # Proses pasien
    print("Pasien diproses:", queue.process_patient())  

    # Tampilkan antrian setelah pemrosesan
    print("Antrian setelah pemrosesan:")
    queue.display_queue()