#@title 3.Get source and target image or video, and start to replace
import os, sys
source = "../content/source.jpg" #@param {type:"string"}
target = "../content/onevideo.mp4" #@param {type:"string"}
output = "../content/myvideo.mp4" #@param {type:"string"}

Device = "cpu" #@param ["cuda", "cpu"]

Processor = "face_swapper" #@param ["face_swapper face_enhancer", "face_swapper","face_enhancer"]

VideoEncoder = "libx264" #@param ["libx264", "libx265","ibvpx-vp9"]

VideoQuality = "18" #@param {type:"string"}

if os.path.exists(source) and os.path.exists(target):
    cmd = f"python run.py --execution-provider {Device} -s {source} -t {target} -o {output} --frame-processor {Processor} --keep-frames --similar-face-distance 3 --keep-fps --execution-threads 16"
    print("cmd:"+cmd)
    print('Starting Image Conversion...')
    os.system(cmd)
    print('Ended Image Conversion...')
    # !python $cmd
else:
    print("Source or target file does not exist.")
