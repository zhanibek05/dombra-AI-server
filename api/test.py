from basic_pitch.inference import predict_and_save
from basic_pitch import ICASSP_2022_MODEL_PATH
import os


output_directory = os.path.abspath(os.path.join("static", "converted"))
#output_directory = "C:/Users/Zhanibek/Desktop/dombra_server/dombra_backend/api/static/output.mid"
#os.makedirs(output_directory, exist_ok=True)

file_path = "C:/Users/Zhanibek/Music/adai.mp3"

save_midi = True
sonify_midi = False
save_model_outputs = False
save_notes = False

predict_and_save(
    [file_path],
    output_directory,
    save_midi,
    sonify_midi,
    save_model_outputs,
    save_notes,
    ICASSP_2022_MODEL_PATH
)
