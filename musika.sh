cd /home/hawau.toyin/Documents/musika

# encode songs
python3 musika_encode.py --files_path /home/hawau.toyin/Documents/amrDiab --save_path /home/hawau.toyin/Documents/encs

# train from scratch using the song encodings the 12sec context window architecture
python musika_train.py --train_path /home/hawau.toyin/Documents/encs

# finetuning musika's checkpoint
python musika_train.py --train_path /home/hawau.toyin/Documents/encs --load_path checkpoints/misc --lr 0.00004

# generate samples
python musika_generate.py --load_path /home/hawau.toyin/Documents/musika/checkpoints/MUSIKA_latlen_256_latdepth_64_sr_44100_time_20230407-145219/MUSIKA_iterations-2259k_losses-0.9273848-0.2040401-0.2008617 \
 --num_samples 4 --seconds 15 --save_path /home/hawau.toyin/Documents/musika/samples/musikaLD/samples


python musika_generate.py --load_path /home/hawau.toyin/Documents/musika/checkpoints/smallLD/MUSIKA_latlen_128_latdepth_64_sr_44100_time_20230505-211256/MUSIKA_iterations-1181k_losses-0.9463728-0.2269291-0.2100470 \
 --num_samples 2 --seconds 15 --save_path /home/hawau.toyin/Documents/musika/samples/smallLD/samples --small True

