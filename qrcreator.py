import pyqrcode

from pyqrcode import QRCode

url = pyqrcode.create("https://colegio433.netlify.app/")
url.svg("portafolio.svg",scale=)