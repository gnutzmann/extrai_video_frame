import os
import cv2
import argparse


def extract_frames(video_file):
    if not os.path.isfile(video_file):
        print(f"Erro: O arquivo '{video_file}' não foi encontrado.")
        return

    video_name = os.path.splitext(os.path.basename(video_file))[0]
    output_dir = os.path.join(os.getcwd(), "image_output", video_name)

    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_file)
    if not cap.isOpened():
        print(
            f"Erro: Não foi possível abrir o arquivo de vídeo '{video_file}'.")
        return

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_filename = os.path.join(
            output_dir, f"frame_{frame_count:04d}.png")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

    cap.release()
    print(f"Extração concluída! Frames salvos em: {output_dir}")


def main():
    parser = argparse.ArgumentParser(
        description="Extrai frames de um arquivo de vídeo.")
    parser.add_argument("video_file", help="Caminho para o arquivo de vídeo.")
    args = parser.parse_args()

    extract_frames(args.video_file)


if __name__ == "__main__":
    main()
