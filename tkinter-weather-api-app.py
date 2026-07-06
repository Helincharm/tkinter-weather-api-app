import tkinter as tk
from PIL import Image, ImageTk
import math
import pygame
from PIL.ImageOps import contain
from pygame import mixer
import requests
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("WEATHER_API_KEY")



class mini_uyg(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("weather_app")
        self.geometry("500x500")
        self.resizable(False, False)

        # karakter kısmı
        self.char_path = "assets/images/helin_chibi.png"
        self.char_x = 500 - 15
        self.char_y = 500 - 15
        self.char_path = "assets/images/helin_chibi.png"
        self.char_size = (110, 110)

        self.char_photo = None
        self.char_id = None

        # karakterin idle animasyonu
        self.float_offset = 0
        self.float_dir = 1
        self.float_max = 6
        self.idle_job = None

        self.canvas = tk.Canvas(self, width=500, height=500, highlightthickness=0)
        self.canvas.place(x=0, y=0)

        self.current_page = 1
        self.total_pages = 6

        mixer.init()

        mixer.music.load("assets/sounds/love_like_you.mp3")

        self.temp_text = None
        self.temp_shadow = None

        mixer.music.play(-1)  #  -1 hep çalıcak demek


        self.render()

    def draw_temperature(self):
        print("draw_temperature çalıştı")

        hava_durumu, sicaklik = self.get_weather()

        if sicaklik is None:
            derece_yazisi = "--°C"
        else:
            derece_yazisi = f"{round(sicaklik)}°C"

        self.canvas.delete("temperature")

        pixel_font = {
            "0": [
                "111",
                "101",
                "101",
                "101",
                "111"
            ],
            "1": [
                "010",
                "110",
                "010",
                "010",
                "111"
            ],
            "2": [
                "111",
                "001",
                "111",
                "100",
                "111"
            ],
            "3": [
                "111",
                "001",
                "111",
                "001",
                "111"
            ],
            "4": [
                "101",
                "101",
                "111",
                "001",
                "001"
            ],
            "5": [
                "111",
                "100",
                "111",
                "001",
                "111"
            ],
            "6": [
                "111",
                "100",
                "111",
                "101",
                "111"
            ],
            "7": [
                "111",
                "001",
                "010",
                "010",
                "010"
            ],
            "8": [
                "111",
                "101",
                "111",
                "101",
                "111"
            ],
            "9": [
                "111",
                "101",
                "111",
                "001",
                "111"
            ],
            "-": [
                "000",
                "000",
                "111",
                "000",
                "000"
            ],
            "°": [
                "110",
                "110",
                "000",
                "000",
                "000"
            ],
            "C": [
                "111",
                "100",
                "100",
                "100",
                "111"
            ]
        }

        def draw_pixel_text(text, x, y, scale=5, color="white", shadow=True):
            start_x = x

            for char in text:
                if char == " ":
                    x += scale * 4
                    continue

                pattern = pixel_font.get(char)

                if pattern is None:
                    x += scale * 4
                    continue

                for row_index, row in enumerate(pattern):
                    for col_index, pixel in enumerate(row):
                        if pixel == "1":
                            px = x + col_index * scale
                            py = y + row_index * scale

                            if shadow:
                                self.canvas.create_rectangle(
                                    px + 2,
                                    py + 2,
                                    px + scale + 1,
                                    py + scale + 1,
                                    fill="black",
                                    outline="black",
                                    tags="temperature"
                                )

                            self.canvas.create_rectangle(
                                px,
                                py,
                                px + scale - 1,
                                py + scale - 1,
                                fill=color,
                                outline=color,
                                tags="temperature"
                            )

                x += scale * 4

        draw_pixel_text(derece_yazisi, 20, 20, scale=5, color="white")

        self.canvas.tag_raise("temperature")

    def show_weather_page(self, event=None):
        main, desc = self.get_weather_main_desc()

        # default giriş sayfam
        if main is None:
            self.current_page = 1  # giriş weather sayfası


        # sunny
        if main == "Clear":
            self.current_page = 2

        #cloudy
        elif main == "Clouds":
            d = (desc or "").lower()
            if "few clouds" in d or "scattered clouds" in d:
                self.current_page = 6  # cloudy_sunny
            else:
                self.current_page = 3  # cloudy

        # rainy
        elif main in ("Rain", "Drizzle", "Thunderstorm"):
            self.current_page = 4

        # snowy
        elif main == "Snow":
            self.current_page = 5

        # başka eklemek istersem:
        else:
            self.current_page = 1 #weather yazılı page

        self.render()

    def render(self):
        self.stop_idle()

        self.canvas.delete("all")

        pages = [
            self.draw_page1,
            self.draw_page2,
            self.draw_page3,
            self.draw_page4,
            self.draw_page5,
            self.draw_page6
        ]

        pages[self.current_page - 1]()

        self.draw_character()

        if self.current_page in (1, 2, 3, 4, 5, 6):
            self.draw_temperature()

        self.start_idle()


    def next_page(self, event=None):
        self.current_page += 1
        self.canvas.tag_bind("next_btn", "<Button-1>", self.show_weather_page)
        self.render()

        #her sayfaynın kendi içeriğini ekle kendine

    #     data kısmı

    def get_weather(self):
        city = "Istanbul"

        if not API_KEY:
            print("API_KEY bulunamadı. .env okunmuyor olabilir.")
            return None, None

        base_url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}"
            f"&appid={API_KEY}"
            f"&units=metric"
            f"&lang=tr"
        )

        try:
            r = requests.get(base_url, timeout=10)
        except requests.RequestException as e:
            print("Request hatası:", e)
            return None, None

        print("Weather API status:", r.status_code)

        if r.status_code != 200:
            print("Weather API cevabı:", r.text)
            return None, None

        data = r.json()

        hava_durumu = data["weather"][0]["main"]
        sicaklik = data["main"]["temp"]

        print("Gelen sıcaklık:", sicaklik)

        return hava_durumu, sicaklik

    def draw_character(self):
        if self.char_photo is None:
            img = Image.open(self.char_path).convert("RGBA")
            img = img.resize(self.char_size)
            self.char_photo = ImageTk.PhotoImage(img)

        def get_weather(self):
            city = "Istanbul"

            print("API_KEY bulundu mu:", API_KEY is not None)
            print("API_KEY boş mu:", API_KEY == "")

            base_url = (
                f"https://api.openweathermap.org/data/2.5/weather"
                f"?q={city}"
                f"&appid={API_KEY}"
                f"&units=metric"
                f"&lang=tr"
            )

            try:
                r = requests.get(base_url, timeout=10)
            except requests.RequestException as e:
                print("Request hatası:", e)
                return None, None

            print("Weather API status:", r.status_code)

            if r.status_code != 200:
                print("Weather API cevabı:", r.text)
                return None, None

            data = r.json()

            hava_durumu = data["weather"][0]["main"]
            sicaklik = data["main"]["temp"]

            print("Gelen sıcaklık:", sicaklik)

            return hava_durumu, sicaklik

        self.char_id = self.canvas.create_image(
            self.char_x, self.char_y,
            image=self.char_photo,
            anchor="se",
            tags=("char",)
        )

    def start_idle(self):
        if self.char_id is None:
            return
        self.animate_idle()

    def stop_idle(self):
        if self.idle_job is not None:
            self.after_cancel(self.idle_job)
            self.idle_job = None

    def animate_idle(self):
        if self.char_id is None:
            return

        self.float_offset += self.float_dir
        if self.float_offset >= self.float_max:
            self.float_dir = -1
        elif self.float_offset <= 0:
            self.float_dir = 1

        x = self.char_x
        y = self.char_y - self.float_offset
        self.canvas.coords(self.char_id, x, y)

        self.idle_job = self.after(60, self.animate_idle)



    def draw_page1(self):
        # arkaplan köprü
        arkaplan_resim = Image.open("assets/images/pixil-frame-0.png")
        arkaplan_resim = arkaplan_resim.resize((500, 500))
        self.arkaplan_foto = ImageTk.PhotoImage(arkaplan_resim)

        self.canvas.create_image(
            0, 0,
            image=self.arkaplan_foto,
            anchor="nw"
        )

        # weather yazısı
        weather_yazisi= Image.open("assets/texts/text_weather.png")
        weather_yazisi = weather_yazisi.resize((350, 400))
        self.weather_yazisi = ImageTk.PhotoImage(weather_yazisi)

        self.canvas.create_image(
            250, 120,
            image=self.weather_yazisi,
            anchor="center"
        )

        # buton da ilk sayfada olacak
        self.draw_next_button()

    def draw_next_button(self):
        buton_resim = Image.open("assets/texts/button1.png")
        buton_resim = buton_resim.resize((200, 200))
        self.next_btn_img = ImageTk.PhotoImage(buton_resim)

        self.canvas.create_image(
        250, 450,
        image=self.next_btn_img,
        tags=("next_btn",)
            )

        self.canvas.tag_bind("next_btn", "<Button-1>", self.next_page)

    def draw_page2(self):
        self.canvas.create_text(250, 250, text="sunny", fill="white", font=("Arial", 24))


        # güneşli arkaplan
        sunny_resmi = Image.open("assets/images/sunny.png")
        sunny_resmi = sunny_resmi.resize((520, 520))
        self.sunny_resmi = ImageTk.PhotoImage(sunny_resmi)

        self.canvas.create_image(
            250, 250,
            image=self.sunny_resmi,
            anchor="center"
        )

        # sunny yazısı
        sunny_yazısı = Image.open("assets/texts/sunny_text.png")
        sunny_yazısı = sunny_yazısı.resize((350, 400))
        self.sunny_yazısı = ImageTk.PhotoImage(sunny_yazısı)

        self.canvas.create_image(
            -10, 250,
            image=self.sunny_yazısı,
            anchor="nw"
        )

    def draw_page3(self):
        self.canvas.create_text(250, 250, text="cloudy", fill="white", font=("Arial", 24))

        # bulutlu arkaplanım
        cloudy_resmi = Image.open("assets/images/cloudy.png")
        cloudy_resmi = cloudy_resmi.resize((500, 500))
        self.cloudy_resmi = ImageTk.PhotoImage(cloudy_resmi)

        self.canvas.create_image(
            250, 250,
            image=self.cloudy_resmi,
            anchor="nw"
        )

        # cloudy yazısı
        cloudy_yazısı = Image.open("assets/texts/cloudy_text.png")
        cloudy_yazısı = cloudy_yazısı.resize((350, 400))
        self.cloudy_yazısı = ImageTk.PhotoImage(cloudy_yazısı)

        self.canvas.create_image(
            -10, 250,
            image=self.cloudy_yazısı,
            anchor="nw")


    def draw_page4(self):
        self.canvas.create_text(250, 250, text="rainy", fill="white", font=("Arial", 24))

        # rainy arkaplan
        rainy_resmi = Image.open("rainy_resmi.png")
        rainy_resmi = rainy_resmi.resize((500, 500))
        self.rainy_resmi = ImageTk.PhotoImage(rainy_resmi)

        self.canvas.create_image(
            250, 250,
            image=self.rainy_resmi,
            anchor="nw"
        )

        # rainy yazısı
        rainy_yazısı = Image.open("assets/texts/rainy_text.png")
        rainy_yazısı = rainy_yazısı.resize((350, 400))
        self.rainy_yazısı = ImageTk.PhotoImage(rainy_yazısı)

        self.canvas.create_image(
            -10, 250,
            image=self.rainy_yazısı,
            anchor="nw")

    def draw_page5(self):
        self.canvas.create_text(250, 250, text="snowy", fill="white", font=("Arial", 24))

        # snowy arkaplan
        snowy_resmi = Image.open("assets/images/snowy.png")
        snowy_resmi = snowy_resmi.resize((500, 500))
        self.snowy_resmi = ImageTk.PhotoImage(snowy_resmi)

        self.canvas.create_image(
            250, 250,
            image=self.snowy_resmi,
            anchor="nw"
        )

        # snowy yazısı
        snowy_yazısı = Image.open("assets/texts/snowy_text.png")
        snowy_yazısı = snowy_yazısı.resize((350, 400))
        self.snowy_yazısı = ImageTk.PhotoImage(snowy_yazısı)

        self.canvas.create_image(
            -10, 250,
            image=self.snowy_yazısı,
            anchor=" nw")

    def draw_page6(self):
        self.canvas.create_text(250, 250, text="cloudy_sunny", fill="white", font=("Arial", 24))

        # cloudy ve sunny arkaplan
        cloudy_sunny_resmi = Image.open("assets/images/cloudy_sunny.png")
        cloudy_sunny_resmi = cloudy_sunny_resmi.resize((500, 500))
        self.cloudy_sunny_resmi = ImageTk.PhotoImage(cloudy_sunny_resmi)

        self.canvas.create_image(
            250, 250,
            image=self.cloudy_sunny_resmi,
            anchor="nw"
        )

        # cloudy_sunny yazısı
        cloudy_sunny_yazısı = Image.open("assets/texts/cloudy_sunny_yazısı.png")
        cloudy_sunny_yazısı = cloudy_sunny_yazısı.resize((350, 400))
        self.cloudy_sunny_yazısı = ImageTk.PhotoImage(cloudy_sunny_yazısı)

        self.canvas.create_image(
            -10, 250,
            image=self.cloudy_sunny_yazısı,
            anchor="nw")




 # if __name__ == "__main__":
 #     uygulama = mini_uyg()
 #     uygulama.mainloop()

if __name__ == "__main__":
    uygulama = mini_uyg()
    uygulama.mainloop()