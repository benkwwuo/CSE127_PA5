#!/bin/bash
cat << "EOF" | openssl dgst -sha256 > DIGEST 
       �"��:{Oɩ���>�6��ݒ���V�����������J�9�-񂊦P�ܻ�J(p�R/�?��oD���aZ�5�����(���\u�4.�5���ڒ��{��TZ�xU�Ճw��H���
EOF
digest=$(cat DIGEST | sed 's/(stdin)= //' )
echo "The sha256 digest is $digest"