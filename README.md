# TangerangPy Coding Challenge

github repository untuk menyimpan coding challenge di telegram tangerang py

## Bagaimana cara menggunakan repository ini??
Pertama-tama tentukan target kalian:

1. [Saya mau share solusi coding challenge saya](#saya-mau-share-solusi-coding-challenge-saya)

2. [Saya mau kontribusi soal coding challenge](#saya-mau-kontribusi-soal-coding-challenge)

3. [Saya menemukan bug, typo di soal coding challenge atau dokumentasi kurang lengkap](#saya-nemu-bug--typo-di-soal-coding-challenge-atau-dokumentasi-kurang-lengkap)


PERHATIAN: Selama kalian mematuhi [code of conduct](./code-of-conduct.md). Jangan takut berbuat salah ketika kontribusi ke repo ini. Jika terjadi kesalahan admin atau github bot akan memberi tahu letak kesalahan kalian. Jadikan repo ini sebagai sarana belajar kalian. Salah satunya bagaimana cara berkontribusi ke open source. 


## Cara Instalasi
### Requirement
- python 3
- pip

### Tahap Instalasi
1. fork repository ini ke github kalian ([how to fork github repo](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo))
1. clone repository hasil fork
1. masuk ke folder repository lalu buat virtual environtment dengan name env `python -m venv env`
1. aktifkan virtual enviroment yg baru di buat `source env/bin/activate`
1. install depedencies `pip install -r requirements.txt`


## Saya mau share solusi coding challenge saya
1. Ikuti [tahap instalasi](#cara-instalasi)
1. buat branch baru dengan format nama branch jawaban/{nama-coding-challenge}-{nama-kalian} lalu ganti branch ke branch yang baru kalian buat
1. masuk ke folder coding challenge yang ingin kalian kerjakan
1. copy file template_jawaban.py ke folder jawaban dengan name jawaban_{nama_kalian}.py (contoh jawaban/jawaban_bima_adi.py)
1. isi file jawaban_{nama_kalian}.py dengan jawaban dari coding challenge kalian
1. jalankan testing `pytest .` pastikan tidak ada error
1. commit perubahan
1. push perubahan ke github repo kalian
1. buat pull request ke repo tangerang py
1. jika sudah memenuhi tahapan diatas admin tangerang py akan review / accept pull request kalian


## Saya mau kontribusi soal coding challenge
1. Ikuti [tahap instalasi](#cara-instalasi)
2. buat branch baru dengan format nama branch add-coding-challenge/{nama-coding-challenge}-{nama-kalian} lalu ganti branch ke branch yang baru kalian buat
3. ikuti struktur koding challenge (bisa lihat di folder contoh_coding_challenge)
```
{folder nama coding challenge}/
    __init__.py
    pertanyaan.md <- berisi soal coding challenge
    template_jawaban.py <- berisi test case untuk coding challenge sebagai referensi jawaban
    jawaban/ <- folder menyimpan jawaban
        __init__.py
```
4. commit perubahan
5. push perubahan ke github repo kalian
6. buat pull request ke repo tangerang py
7. jika sudah memenuhi tahapan diatas admin tangerang py akan review / accept pull request kalian


## Saya nemu bug / typo di soal coding challenge atau dokumentasi kurang lengkap
1. Ikuti [tahap instalasi](#cara-instalasi)
1. buat branch baru dengan format nama branch bug-feature/{judul bug} lalu ganti branch ke branch yang baru kalian buat
1. Fix bug / typo di branch tersebut
4. commit perubahan
5. push perubahan ke github repo kalian
6. buat pull request ke repo tangerang py, tambahkan deskripsi di pull request kalian yg menjelaskan bug atau typo yang kalian kerjakan
7. jika sudah memenuhi tahapan diatas admin tangerang py akan review / accept pull request kalian
