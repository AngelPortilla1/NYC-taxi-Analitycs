import os
import requests
from pathlib import Path
from typing import List
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class TaxiDataExtractor:
    def __init__(self, base_url: str, download_dir: Path):
        self.base_url = base_url
        self.download_dir = download_dir
        self.download_dir.mkdir(parents=True, exist_ok=True)

    def generate_urls(self, year: int, months: List[int]) -> List[str]:
        """
        Genera las URLs dinámicas para los meses solicitados.
        Ej: https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet
        """
        # TODO: Implementar la generación de URLs con f-strings formateando a 2 dígitos el mes
        pass

    def download_parquet(self, url: str) -> None:
        """
        Descarga el archivo en chunks para no saturar la memoria.
        """
        filename = url.split("/")[-1]
        filepath = self.download_dir / filename
        
        # TODO: Implementar validación de existencia de archivo y descarga con requests.get(stream=True)
        pass

    def run_extraction(self, year: int, months: List[int]) -> None:
        urls = self.generate_urls(year, months)
        for url in urls:
            self.download_parquet(url)

if __name__ == "__main__":
    # Configuración quemada por ahora, luego la movemos a config.py
    BASE_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data"
    RAW_DIR = Path("../data/raw")
    
    extractor = TaxiDataExtractor(BASE_URL, RAW_DIR)
    extractor.run_extraction(year=2023, months=[1, 2, 3])