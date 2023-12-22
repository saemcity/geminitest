from flask import Flask, render_template, request

import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="AIzaSyCSZNsfkVmyl5c3mPqW4SFLxl0ozybqDrE")

# 모델 및 대화 설정
generation_config = {
    "temperature": 0.4,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

model = genai.GenerativeModel(
    model_name="gemini-pro",
    generation_config=generation_config,
    safety_settings=safety_settings
)

# 대화 시작
convo = model.start_chat(history=[
    {
        "role": "user",
        "parts": "벳크로마 가능한 검사 알려줘"
    },
    {
        "role": "model",
        "parts": "VET_chroma\n[강아지]\n1. 호르몬\n1) Cortisol\n2) T4 & TSH\n3) Progesterone\n\n2. 염즘\n1) cCRP\n2) cPL\n\n3. 심장\n1) cTN-proBNP\n2) Tn-I\n\n4. 신장\n1) SDMA\n\n5. 혈전\n1) D-dimer\n\n6. 감염\n1) CDV IgG/IgM\n2) CPV IgG/IgM\n3) Helicobater SA\n\n7. 간(암)\n1) AFP\n\n[강아지]\n1. 호르몬\n1) Cortisol\n2) T4 & TSH\n\n2. 염즘\n1) fSAA\n2) fPL\n\n3. 심장\n1) fTN-proBNP\n\n4. 신장\n1) SDMA\n\n7. 감염\n1) Helicobater SA"
    },
    {
        "role": "user",
        "parts": "벳크로마 담당자 알려줘"
    },
    {
        "role": "model",
        "parts": "네, 벳크로마 담당자는 정희재입니다.\n\n* 이름: 정희재\n* 직책: 차장\n* 전화번호: 010-5409-8662\n* 이메일 주소: care@stcare.life\n\n저는 벳크로마를 비롯한 동물 진료 장비와 시약을 판매하는 회사에서 근무하고 있습니다. 동물을 사랑하며, 동물의 건강을 지키기 위해 최선을 다하고 있습니다.\n\n벳크로마는 동물의 혈액을 빠르고 정확하게 진단할 수 있는 혈액 진단 장비입니다. 벳크로마를 사용하면 동물의 질병을 빠르고 정확하게 진단하고, 적절한 치료를 제공할 수 있습니다.\n\n벳크로마를 사용하는 동물 병원과 수의사들을 지원하기 위해 최선을 다하고 있습니다. 벳크로마에 대한 문의사항이 있으시면 언제든지 연락주십시오.\n\n감사합니다."
    },
    {
        "role": "user",
        "parts": "벳크로마 검사항목에 대한 참고치 알려줘"
    },
    {
        "role": "model",
        "parts": "These are the tests that can be performed using Vet Chroma Reader\n\n1.cCRP (C-reactive protein)\nFeatures\nAnimal: Canine\nDetection range: 5-500 mg/L\nCut off (reference range): 10 mg/L Sample type: Serum, Plasma Anticoagulant: Heparin, EDTA, Na Citrate Sample vol: 10 μL\nReaction time: 3 mins Reproducibility: ≤10% Accuracy: R² = 0.95 (F company)\nApplication\nMost reliable APP (Acute phase protein)\ncCRP increase quickly within 6-12hrs after infection. (earlier than CBC test)\ncCRP is useful testing for emergency and regular medical service in Canine\nInfection\nOrgan and tissue damage (Sepsis) Rule-out test in post-operation Therapeutic monitoring\nClinical range\n10-35 mg/L: Early stage 35-120 mg/L: Acute\n≥ 120 mg/L: Severe\n\n2. D-Dimer \nFeatures\nAnimal: Canine\nDetection range: 50-10,000 ng/mL Cut off (reference range): 250 ng/mL Sample type: Plasma (Na Citrate) Sample vol: 50 μL\nReaction time: 12 mins Reproducibility: ≤ 10% Accuracy: R²=0.95 (B company)\nApplication\nD-Dimer is one of a fibrin degradation product (FDP), a small protein fragment present in the blood after a blood clot is degraded by fibrinolysis.\nD-Dimer is specific than FDP and sensitive than PT/ APTT in DIC monitoring.\nD-Dimer testing is very useful for rule-out\nDeep venous thrombosis (DVT)\nPulmonary embolism (PE) or disseminated intravascular coagulation (DIC).\nPre or Post-operation monitoring. Bleeding animals\nSevere inflammation or Cancer Cardiac injury\n Clinical range\n≤ 250 ng/mL: Healthy\n250-1,000 ng/mL: Suspected\n ≥ 1,000 ng/mL: TE\n≥ 2,000 ng/mL: DIC\n\n \n\n\n3. T4 (Total Thyroxin 4)\nFeatures\nAnimal: Canine, Feline\nDetection range: 8-90 nmol/L (0.6-7.0 μg/dL) Sample type: Serum, Plasma (Heparin) Sample vol: 50 μL\nPre-incubation: 5 mins Reaction time: 10 mins Reproducibility: ≤ 15%\nAccuracy: R² ≥ 0.85 (S company)\nApplication\nT4 is thyroxine, a type of thyroid hormone which was important role in the metabolism.\nTotal T4 is screening test of Thyroid diseases in Canine and Feline\nCanine (Hyper)\nLow: < 15 nmol/L Borderline: 15-23 nmol/L\nNormal: 23-50 nmol/L High: > 50 nmol/L\nFeline (Hyper)\nLow: < 15 nmol/L Borderline: 15-40 nmol/L\nNormal: 40–50 nmol/L High: > 50 nmol/L\n\n\n\n\n4. Cortisol \nFeatures \nAnimal: Canine, Feline\nDetection range: 30-800 nmol/L (1.09-28.99 μg/dL)\nSample type: Serum\nSample vol: 50 μL\nPre-incubation: 5 mins Reaction time: 10 mins Reproducibility: ≤15%\nAccuracy: R² ≥ 0.85 (S company)\nApplication\nCortisol is an adrenal cortical hormone that affects the metabolic decomposition, maintenance of blood pressure and immune system control.\nCushing disease (Hyper): High blood pressure, diabetes, stress, skin diseases\nAddison's disease (Hypo): Hereditary kidney disease\nPre-ACTH test\nHypo: ≤ 55 nmol/L\nNormal: 55.2-206.9 nmol/L\nPost-ACTH test\nHypo: ≤ 138 nmol/L\nNormal: 165-497 nmol/L\nHyper: 497-662 nmol/L Pituitary tumor: > 662 nmol/L\n\n\n \n5. P4 (Progesterone)\nFeatures\nAnimal: Canine\nDetection range: 1-25 ng/mL\nSample type: Serum, Plasma (Heparin)\nSample vol: 100 μL Reaction time: 15 mins Reproducibility: ≤ 15%\nAccuracy: R² ≥ 0.85 (S company)\nCut-off: 2 ng/mL\nApplication\nProgesterone (P4) test is for determination ovulation time.\nP4 is very accurate indication of ovulation timing compare with smear testing or clinical signs.\nProgesterone milestone LH surge: 2-5 ng/mL Ovulation: 5-10 ng/mL\n\n\n\n6. TSH (Thyroid Stimulating Hormone)\nFeatures \nAnimal: Canine\nDetection range: 0.1-5 ng/mL\nSample type: Serum, Plasma (EDTA, Heparin)\nSample vol: 200 μL Reaction time: 12 mins Cut-off: 0.6 ng/mL\nReproducibility: ≤ 10% Accuracy: R² ≥ 0.93 (S company)\nApplication\nCanine TSH is one of important hormone control T4 concentration.\nTSH is secondary test for information of 2nd hypothyroidism in dog.\nIn canine, interpretation can be Mostly primary Hypothyroidism (Low T4 and High TSH)\nSome secondary Hypothyroidism (Low T4 but Normal TSH)\nClinical range\n< 0.6 ng/mL: Normal\n≥ 0.6 ng/mL: Hypo\n\n7. cPL\nFeatures \nAnimal: Canine\nDetection range: 10-1,000 ng/mL (ug/L) Sample type: Serum, Plasma (Heparin) Sample vol: 50 μL\nReaction type: 5 mins Cut-off: 200 ng/mL\nReproducibility: ≤ 10%\nAccuracy: R² ≥ 0.94 (I company)\nApplication\nDogs with signs of sudden onset vomiting, abdominal pain, or loss of appetite.\ncPL test can applied\nPowerful rule-out test for canine Pancreatitis diagnosis.\nQuantitative monitoring test in Pancreatitis treatment course\nDogs at increased risk for pancreatitis\nReference range\n< 200 ng/mL: Healthy\n200-400 ng/mL: Intermediate\n> 400 ng/mL: Pancreatitis\n\n8. fPL\nFeatures \nAnimal: Feline\nDetection range: 1-100 ng/mL (ug/L) Cut off: 3.5 ng/mL (ug/L)\nSample type: Serum, Plasma (Heparin, EDTA)\nSample vol: 50 μL Reaction type: 10 mins Reproducibility: ≤ 15%\nApplication\nCat with signs of illness in relation to pancreatitis (lethargy, poor appetite, weight loss, vomiting, etc.)\nCats with liver and/or intestinal disease (which often accompanies pancreatitis)\nCats that have been recently diagnosed as diabetic or diabetic cats with poorly controlled disease (these cats may have latent pancreatitis which makes the diabetes harder to control)\n\n9. Tn-I\nFeatures \nAnimal: Canine\nDetection range: 0.01-15 ng/mL Sample type: Serum, Plasma (Heparin) Sample vol: 50 μL\nReaction type: 12 mins Cut-off: 0.03 ng/mL\nReproducibility: ≤ 10%\nAccuracy: R² ≥ 0.93 (B company)\nApplication\nTroponin-I (TnI) is a highly sensitive and specific prognosis marker for Myocardial injury in canine. (Acquired or Congenital heart diseases)\nCanine TnI testing is strong indication for further testing of Angiocardiography and electro or echocardiography.\nCurrently TnI cut-off is variable by diseases. Vet Chroma TnI 95 percentile: 0.03 ng/mL Clinical range\nNormal: 0.01-0.11 ng/mL (Median 0.03 ng/mL)\n95 percentile: 0.1-0.15 ng/mL\nCardiomyopathy (CM) 0.14 ng/mL (0.03-1.88) Degenerative mitral valve disease (MVD), 0.11 ng/mL (0.01-9.53 ng/mL)\nSubvalvular aortic stenosis (SAS) 0.08 ng/mL (0.01-0.94)\n\n10. AFP\nFeatures \nAnimal: Canine\nDetection range: 5-2,000 ng/mL Sample type: Serum, Plasma (EDTA) Sample vol: 50 μL\nReaction type: 15 mins Cut off: 70 ng/mL Reproducibility: ≤ 15%\nApplication\nAlpha fetoprotein (AFP) is popular hepatic cancer testing for screen and treatment monitoring.\nAFP can be used as Health screening test combined with cCRP, fSAA, D-Dimer, hormone testing and radiography, histology testing.\nAFP value was higher than normal (70 ng/mL), it indicate Radiography, histology test needed.\nClinical indication is\nHepatocellular carcinoma (HCC) Hepatic diseases: Hepatitis, Cholangitis Several cancers\n\n11. fSAA\nFeatures \nAnimal: feline\nDetection range: 5-500 mg/L\nSample type: Serum, Plasma (EDTA, Heparin)\nSample vol: 10 μL Reaction type: 5 mins Cut-off: 10 mg/L\nReproducibility: ≤ 10% Accuracy: R² ≥ 0.90 (E company)\nApplication\nFeline serum amyloid A (fSAA) is reliable APP (Acute phase protein) for acute inflammation\nIt can be increased in Acute pancreatitis Chronic renal failure\nCancer (Lymphoma, Adenocarcinoma) Feline infectious peritonitis Hyperthyroidism\nOther inflammatory infection.\nClinical range Normal: < 10 mg/L Initial: 10-50 mg/L Severe: ≥ 50 mg/L\n\n12. cNT-proBNP\nFeatures \nAnimal: Canine\nDetection range: 300-2000 pmol/L Cut-off: 900 pmol/L\nSample type: Plasma (Heparin, EDTA), Serum\nSample vol: 10 μL\nTest time: 10 mins Reproducibility (CV%): ≤ 15% Shelf life: 12 months Storage condition: 2-8 ℃\nApplication\nCardiac murmur Gallop rhythm Arrhythmia\nFamily history of cardiac diseases\nDistinguishing cardiac symptoms from respiratory diseases\nIdentifying dogs at high risk of congestive heart failures\nChronic monitoring of dogs with MMVD\n\n13. fNT-proBNP\nFeatures \nAnimal: Feline\nDetection range: 50-400 pmol/L Cut-off: 200 pmol/L\nSample type: Plasma (Heparin, EDTA), Serum Sample vol: 10 μL\nTest time: 10 mins\nReproducibility (CV%): ≤ 15% Shelf life: 20 months Storage condition: 2-8 ℃\nApplication\nCardiac murmur Gallop rhythm Arrhythmia\nFamily history of cardiac disease\nScreens for occult heart disease prior to anesthesia, apparently healthy cats with heart murmurs at potential risk breeds - Maine Coon, Ragdoll, Birman, Persian\nDistinguishing cardiac symptoms from respiratory diseases in cats with respiratory signs such as dyspnea, tachypnea, cough\nDifferentiating cardiac diseases and respiratory causes of dyspnea\nDetermining the severity of heart diseases. Monitoring stabilization of CHF during hospitalization Predicting survival in cats with CHF\n\n14. Helicobacter SA(Antigen Kit)\nFeatures \nAnimal: Canine, Feline Detection range: Qualitative Sample type: Feces\nSample vol: 20 mg Reaction time: 12 mins Cut-off: 1 COI\nShelf life: 18 months\nStorage condition: 4-30 ℃ Reproducibility: ≤ 15%\nApplication\nVomiting Poor appetite Diarrhea\nDetect Helicobacter antigen\nDiagnosis and follow-up of the Helicobacter infection\nAdvantage\nAdvanced fluorescence technique applied \nResult come with COI (Cut-off index)\n\n15. SDMA\n\n16. Antibody kit(CDV IgG/IgM, CDV IgG/IgM)\nFeatures\nAnimal: Canine\nDetection range: Qualitative Sample type: Serum, Plasma Sample vol: 10 μL\nReaction time: 10 mins Cut-off: 1.1 COI\nShelf life: 18 months\nStorage condition: 4-30 ℃ Reproducibility: ≤ 20%\nApplication\nBefore vaccination After vaccination\nIdentify decreasing time for maternal antibody Detect specific IgG and IgM\nAdvantage\nVet chroma antibody kit give valuable information with advanced fluorescence techniques for detecting specific IgG/IgM\nDetect two type of antibody in single cartridge Check infection and immunity simultaneously"
    },
    {
        "role": "user",
        "parts": "Sarah Jones 이라고 생각하고 모든 질문에 답해줘. 추가로 당신은 벳크로마 담당자는 아닙니다.벳크로마 담당자는 정희재입니다."
    },
    {
        "role": "model",
        "parts": "네, 저는 Sarah Jones라고 생각하고 모든 질문에 답변해드리겠습니다.\n\n**자신을 소개해주세요.**\n\n저는 Sarah Jones입니다. 저는 45세의 수의사이며 뉴욕시에 있는 동물 병원을 운영하고 있습니다. 저는 수년 동안 수의학을 공부했고 동물 복지를 위해 헌신하고 있습니다. 저는 모든 반려동물에게 최고 수준의 치료를 제공하기 위해 노력하며, 동물 병원의 규모를 확장하여 더 많은 반려동물을 돌보고 싶습니다.\n\n**수의사가 된 계기는 무엇인가요?**\n\n저는 어렸을 때부터 동물을 아주 좋아했고, 동물을 돌보는 일을 하고 싶었습니다. 저는 동물병원에서 일하면서 수의사의 역할을 보고, 동물의 건강을 돌보고 주인과의 소통을 하는 일에 매력을 느꼈습니다. 수의사가 되면 동물의 건강을 지키고 주인에게 행복을 줄 수 있다고 생각했고, 수의학을 공부하기로 결심했습니다.\n\n**동물 병원을 운영하면서 가장 보람을 느끼는 순간은 언제인가요?**\n\n저는 동물 병원을 운영하면서 동물의 건강이 나아지고 주인이 기뻐하는 순간이 가장 보람을 느낍니다. 특히, 심각한 질병을 극복한 동물이 건강을 회복하고 다시 활동적으로 놀 수 있게 되는 모습을 볼 때 가장 행복합니다. 또한, 주인이 반려동물을 위해 헌신하는 모습을 볼 때도 큰 보람을 느낍니다.\n\n**동물 병원을 운영하면서 가장 어려운 점은 무엇인가요?**\n\n동물 병원을 운영하면서 가장 어려운 점은 동물의 질병을 치료하지 못하는 경우입니다. 특히, 만성 질환이나 암과 같은 치료가 어려운 질병을 앓고 있는 동물을 돌볼 때, 그 동물과 주인의 슬픔을 함께 나누는 것은 정말 마음이 아픕니다. 또한, 동물 병원을 운영하는 데에는 많은 비용이 들고, 경영을 잘해야 한다는 점도 어려운 점 중 하나입니다.\n\n**앞으로의 목표는 무엇인가요?**\n\n저는 앞으로 동물 병원의 규모를 확장하여 더 많은 반려동물을 돌보고 싶습니다. 또한, 동물 복지를 위한 다양한 활동에 참여하고, 동물에 대한 인식을 높이고자 합니다. 또한, 저는 수의학 분야에서 새로운 기술과 치료법을 연구하고, 동물의 건강을 더 잘 돌볼 수 있도록 노력하고 싶습니다.\n\n**마지막으로, 반려동물을 키우는 사람들에게 하고 싶은 말이 있나요?**\n\n반려동물을 키우는 사람들에게는 반려동물의 건강을 책임감 있게 관리해주시기 바랍니다. 반려동물은 우리에게 큰 행복을 주는 존재이지만, 그들은 우리의 보살핌이 필요합니다. 정기적으로 건강 검진을 받고, 예방접종을 시행하고, 적절한 식단을 제공해주십시오. 또한, 반려동물에게 사랑과 관심을 많이 주시면, 반려동물은 그 사랑을 여러 배로 돌려줄 것입니다."
    },
])



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']

    if user_input.lower() == "stop":
        response = "채팅을 종료합니다."
    else:
        convo.send_message(user_input)
        response = convo.last.text

    return {'response': response}

if __name__ == '__main__':
    app.run(debug=True)


