# Como exportar o app para APK (Android) usando Capacitor

## Pré-requisitos
- Node.js e npm instalados
- Android Studio instalado

## Passos

1. **Instale o Capacitor no frontend:**
   ```sh
   cd frontend
   npm install @capacitor/core @capacitor/cli
   npx cap init py-learn com.pylearn.app --web-dir=build
   ```

2. **Gere o build do React:**
   ```sh
   npm run build
   ```

3. **Adicione a plataforma Android:**
   ```sh
   npx cap add android
   ```

4. **Abra no Android Studio:**
   ```sh
   npx cap open android
   ```

5. **No Android Studio:**
   - Aguarde o sync do projeto.
   - Clique em "Build > Build Bundle(s) / APK(s) > Build APK(s)".
   - O APK estará disponível na pasta `app/build/outputs/apk/`.

## Dicas para mobile
- Certifique-se de que o backend esteja acessível via IP local ou domínio público.
- Ajuste o layout para responsividade (mobile-first).
- Personalize ícone e splash screen em `android/app/src/main/res`.
- Teste em emulador e dispositivo real.

---

Se precisar de scripts automáticos ou integração com push notification, permissões, etc, peça aqui!
