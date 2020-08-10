#alias to use on fish shell to create conda env given name, with prefixed template
function conda_ds_init -d "Conda init using name from input and a data science yml template"
    sed -i.bak "4s/.*/name: $argv/" ~/anaconda3/bin/anaconda_ds_env.yml
    conda env create -f ~/anaconda3/bin/anaconda_ds_env.yml
    sed -i.bak "4s/.*/name: /" ~/anaconda3/bin/anaconda_ds_env.yml
    rm ~/anaconda3/bin/anaconda_ds_env.yml.bak
    conda activate $argv
end 
funcsave conda_ds_init

