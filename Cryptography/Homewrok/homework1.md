# Homework 1

SA18225036 陈旻

## Section 1

1. What is the OSI security architecture? 什么是OSI安全架构？

   The OSI security architecture focuses on security attacks, mechanisms, and services. These can be defined briefly as

   - Security attack: Any action that compromises the security of information
     owned by an organization.
   - Security mechanism: A process (or a device incorporating such a process)
     that is designed to detect, prevent, or recover from a security attack.
   - Security service: A processing or communication service that enhances the
     security of the data processing systems and the information transfers of an
     organization. The services are intended to counter security attacks, and they
     make use of one or more security mechanisms to provide the service.

2. List and briefly define categories of security services.  列出并简要定义安全服务的种类。

   - AUTHENTICATION
     - Peer Entity Authentication
     - Data-Origin Authentication
   - ACCESS CONTROL
   - DATA CONFIDENTIALITY
     - Connection Confidentiality
     - Connectionless Confidentiality
     - Selective-Field Confidentiality
     - Traffic-Flow Confidentiality
   - DATA INTEGRITY
     - Connection Integrity with Recovery
     - Connection Integrity without Recovery
     - Selective-Field Connection Integrity
     - Connectionless Integrity
     - Selective-Field Connectionless Integrity
   - NONREPUDIATION
     - Nonrepudiation, Origin
     - Nonrepudiation, Destination

3. List and briefly define categories of security mechanisms.  列出并简要定义安全机制的种类。

   - SPECIFIC SECURITY MECHANISMS
     - Encipherment
     - Digital Signature
     - Access Control
     - Data Integrity
     - Authentication Exchange
     - Traffic Padding
     - Routing Control
     - Notarization
   - PERVASIVE SECURITY MECHANISMS
     - Trusted Functionality
     - Security Label
     - Event Detection
     - Security Audit Trail
     - Security Recovery

## Section 3

1. Describe the five main requirements for the secure use of symmetric encryption. 对称加密方案的五个基成分是什么？并分别给出定义。
   - Plaintext: This is the original intelligible message or data that is fed into the
     algorithm as input.
   - Encryption algorithm: The encryption algorithm performs various substitutions
     and transformations on the plaintext.
   - Secret key: The secret key is also input to the encryption algorithm. The key is
     a value independent of the plaintext and of the algorithm. The algorithm will
     produce a different output depending on the specific key being used at the
     time. The exact substitutions and transformations performed by the algorithm
     depend on the key.
   - Ciphertext: This is the scrambled message produced as output. It depends on
     the plaintext and the secret key. For a given message, two different keys will
     produce two different ciphertexts. The ciphertext is an apparently random
     stream of data and, as it stands, is unintelligible.
   - Decryption algorithm: This is essentially the encryption algorithm run in
     reverse. It takes the ciphertext and the secret key and produces the original
     plaintext.

2. What are the two basic functions used in encryption algorithms? 密码算法中两个基本函数是什么？

   加密算法：![img](file:///C:/Users/Vander/AppData/Local/Temp/msohtmlclip1/01/clip_image002.png)

   解密算法：![img](file:///C:/Users/Vander/AppData/Local/Temp/msohtmlclip1/01/clip_image004.png)

3. What is the difference between a block cipher and a stream cipher? 分组密码和流密码的区别是什么？

   A block cipher processes the input one block of elements at a time, producing an output block for each input block. A stream cipher processes the input elements continuously, producing output one element at a time, as it goes along.

4. What are the two general approaches to attacking a cipher?  攻击密码的两种通用方法是什么？

   Cryptanalytic attack、Brute-force attack

6. List and briefly define types of cryptanalytic attacks based on what is known to the Attacker？列出并简要地定义基于攻击者所知道信息的密码分析攻击类型。

   ![1559228857333](C:\Users\Vander\AppData\Roaming\Typora\typora-user-images\1559228857333.png)

7. What is the difference between an unconditionally secure cipher and a computationally secure cipher? 无条件安全的密码和计算上安全的密码的区别是什么？

   unconditionally secure cipher:无论有多少密文可用，如果方案生成的密文没有足够的信息唯一地确定相应的明文，则无条件地安全；

   computa secure cipher：①破坏密码的代价超过了加密信息的价值。②破解密码所需的时间超过了信息的使用寿命。满足以上两个保准之一的便称为计算机安全

   (如果不论截取者获得了多少密文，达拿在密文中都没有足够的信息来唯一地确定出对应的明文，则这一密码体制称为无条件安全的；

   如果密码体制中的密码不可能被使用的计算机资源破译，则这一密码体制在计算机上是安全的。)

8. Why is the Caesar cipher substitution technique vulnerable to a brute-force cryptanalysis? 为何Caesar容易被暴力破解？
   - 加密和解密算法已知
   - 只有25个字母可以尝试
   - 明文的语言已知且很容易识别

9. How much key space is available when a monoalphabetic substitution cipher is used to replace plaintext with ciphertext?  单表替换密码方法中，密钥空间是多大？

   26!

10. What is the drawback of a Playfair cipher? Playfair密码的缺点是什么？

    它仍谈保留了明文语言的大部分结构，几百个字母的密文通常就足够了，很容易被破解

11. What is the difference between a monoalphabetic cipher and a polyalphabetic cipher? 单表替换密码和多表替换密码的区别是什么？

    单表替换密码只使用一个密文字母表，并且密文字母表中的一个字母来代替一个明文字母表中的一个字母；多表替换密码是将明文消息中出现的同一个字母，在加密时不是完全被同一个固定的字母代换，而是根据其出现的位置次序，用不同的字母代换

12. What are two problems with the one-time pad? 在实际使用中，一次一密存在的两个基本难点是什么？
    - 制作大量随机密钥是一个实际问题。任何频繁使用的系统都可能需要数百万个随机字符;
    - 更令人生畏的是密钥分配和保护问题。对于每个要发送的消息，发送方和接收方都需要一个长度相等的密钥。因此，存在着一个庞大的密钥分配问题。

13. What is a transposition cipher?  什么是置换/乱密码

    一种通过对纯文本字母执行某种排列来实现的一种非同寻常的映射称为置换密码

14. What are the drawbacks of Steganography? 隐写术的缺点是什么？

    隐藏相对少量的信息需要很大的开销，一旦系统被发现，它就变得毫无价值

## Section 4

3. Why is it not practical to use an arbitrary reversible substitution cipher of the kind shown in Table 4.1?        为什么使用表4.1所示的任意可逆替换密码不实际？

   从实现的角度来看，分组长度很大的可逆代换结构时不实际的。如果分组长度太小，系统则等价于古典的代换密码，容易通过对明文的统计分析而被攻破。表4.1定义了n=4时从明文到密文的一个可逆映射，其中第二列是每个明文分组对应的密文分组的值，可用来定义
   这个可逆映射，因此从本质上来说，第二列是从所有可能映射中决定某一特定映射的密钥。这个例子中，密钥需要64比特，。一般地，对n比特的代换结构，密钥的大小是n*2n比特。如对64比特的分组，密钥大小应是64×264=270≈1021比特，因此难以处理

5. What is the difference between diffusion and confusion? 混淆与扩散的差别是什么？

   扩散（diffusion）：将明文的统计特征散布到密文中，实现方式是使得明文的每一位影响密文中多位的值，使得每一个字母在密文中出现的频率比在明文中出现的频率更接近于相等。其目的是使明文和密文之间的统计关系变得尽可能复杂，使敌手无法得到密钥；

   混淆（confusion）：其目的在于使作用于铭文的密钥和密文之间的关系复杂化，是明文和密文之间、密文和密钥之间的统计关系相关特性极小化，从而使统计分析攻击不能奏效。

6. Which parameters and design choices determine the actual algorithm of a Feistel cipher? 哪些参数与设计决定了实际的Feistel密码算法？

   分组长度：分组越长则安全性越高，但加密或解密速度越低，分组长度为64位是一个合理的折衷；

   密钥长度：密钥越长越安全，但加密解密速度越低，64位的密钥已被证明是不安全的，128位是常用的长度；

   迭代次数：迭代越多越安全，通常为16次迭代

   子密钥产生算法：越复杂则密码分析越困难

   轮函数：越复杂则康密码分析的能力越难

## Section *

1. 什么是Feistel密码？为什么说研究Feistel密码很重要？

   Feistel提出利用乘积密码可获得简单的代换密码，乘积密码指顺序地执行两个或多个基本密码系统，使得最后结果的密码强度高于每个基本密码系统产生的如果

2. 什么是乘积密码？

   乘积密码就是以某种连续执行两个或多个简单密码（替代、置换），以使得所得到的最后结果或乘积从密码编码的角度比其中任意一个组成密码都更强的分组密码；

3. 解释什么是雪崩效应。

   雪崩效应就是一种不稳定的平衡状态也是加密算法的一种特征，它指明文或密文的少量变化会引起密文的很大变化，就像雪崩，山上看上去很平静，但是只要有一点点问题，就造成一大片崩溃。可以在很多场合对于hash码，雪崩效应是指少量消息位的变化会引起信息摘要的许多位变化。

4. 习题4.1

   分组密码作用于n位明文分组上，而产生n位密文分组。共有个不同的明文分组，且由于加密是可逆的（即可以解密），每一个明文分组将唯一对应一个密文分组。这样的变换称为可逆变换，或非奇异变换

5. 习题4.7

   快速的软件实现和算法容易分析