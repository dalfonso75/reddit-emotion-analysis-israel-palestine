import sys
import os
import pandas as pd
import torch
import glob

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.sentiment_models import (
    EmotionAnalyzerT5,
    EmotionAnalyzerBERT,
    EmotionAnalyzerDistilBERT,
)

# Verificar dispositivo
device = 0 if torch.cuda.is_available() else -1
print(f"🖥️ Usando dispositivo: {'GPU' if device == 0 else 'CPU'}")

# Inicializar el clasificador
# Agregar el modelo a usar
analyzer = EmotionAnalyzerT5(device=device)

# Configuración de paths
input_path = "data/reddit_opinion_PSE_ISR_cleaned.csv"
chunk_dir = "data/chunks_T5"
final_output = "data/reddit_emotions_T5.csv"
chunk_size = 100_000

# Crear carpeta para chunks si no existe
os.makedirs(chunk_dir, exist_ok=True)

# Determinar los chunks ya procesados
existing_chunks = glob.glob(os.path.join(chunk_dir, "chunk_*.csv"))
processed_indices = set(
    int(os.path.basename(f).split("_")[1].split(".")[0]) for f in existing_chunks
)
print(f"🔁 Ya existen {len(processed_indices)} chunks procesados.")

# Procesar dataset por partes
reader = pd.read_csv(input_path, chunksize=chunk_size)

for i, chunk in enumerate(reader):
    chunk_id = i + 1
    if chunk_id in processed_indices:
        print(f"⏩ Chunk {chunk_id} ya existe, se omite.")
        continue

    print(f"⚙️ Procesando chunk {chunk_id} con {len(chunk)} filas...")
    try:
        chunk_result = analyzer.apply_to_dataframe(chunk, text_column="clean_text")
        chunk_result.to_csv(
            os.path.join(chunk_dir, f"chunk_{chunk_id}.csv"), index=False
        )
        print(f"✅ Chunk {chunk_id} guardado.")
    except Exception as e:
        print(f"❌ Error procesando chunk {chunk_id}: {e}")
        break

# Opcional: unir todos los chunks al final
print("📦 Uniendo todos los chunks...")
all_chunks = sorted(glob.glob(os.path.join(chunk_dir, "chunk_*.csv")))
df_final = pd.concat((pd.read_csv(f) for f in all_chunks), ignore_index=True)
df_final.to_csv(final_output, index=False)
print(f"✅ Archivo final guardado en: {final_output}")
