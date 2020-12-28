### interactive script ###
. generator/setting.sh
#CUDA_VISIBLE_DEVICES=${GPU} fairseq-interactive ${DATA_DIR} \
python generator/interactive-for-japanese.py ${DATA_DIR} \
	--path ${MODEL_DIR}/checkpoint_best.pt \
	--source-lang source \
	--target-lang target \
	--beam 10 \
	--nbest 10 \
	--cpu