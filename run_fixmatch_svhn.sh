# vanilla
python train.py --c config/classic_cv/fixmatch/fixmatch_svhn_1000_0.yaml --use_post_hoc_calib False --n_cal 7810 --n_th 7810 --take_d_cal_th_from eval --loss_reweight False --aug_1 weak --aug_2 strong --gpu 0 --accumulate_pseudo_labels True
# with PLO
python train.py --c config/classic_cv/fixmatch/fixmatch_svhn_1000_0.yaml --use_post_hoc_calib True --n_cal 7810 --n_th 7810 --take_d_cal_th_from eval --loss_reweight False --aug_1 weak --aug_2 strong --gpu 0 --accumulate_pseudo_labels True
