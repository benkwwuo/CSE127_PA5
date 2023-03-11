#!/bin/bash
cat << "EOF" | openssl dgst -sha256 > DIGEST 
       �"��:{Oɩ���>�6��]����V�����������J�9��񂊦P�ܻ�J(��R/�?��oD���aZ�5�����(����\u�4.�5���ڒ��{���Y�xU�Ճw��HR��
EOF
digest=$(cat DIGEST | sed 's/(stdin)= //' )
echo "The sha256 digest is $digest"