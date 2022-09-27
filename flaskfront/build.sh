wget https://github.com/alphagov/govuk-frontend/releases/download/v3.14.0/release-v3.14.0.zip -O govuk_frontend.zip
rm -rf opgflaskfront/static
unzip -o govuk_frontend.zip -d opgflaskfront/static
mv opgflaskfront/static/assets/* opgflaskfront/static
rm -rf opgflaskfront/static/assets
rm -rf govuk_frontend.zip

wget https://github.com/alphagov/govuk-frontend/archive/v3.14.0.zip -O govuk_frontend_source.zip
unzip -o govuk_frontend_source.zip -d govuk_frontend_source
rm -rf govuk_components
mkdir govuk_components
mv govuk_frontend_source/govuk-frontend-3.14.0/package/govuk/components/** govuk_components
find govuk_components -type f ! -name 'fixtures.json' -delete
rm -rf govuk_frontend_source
rm -rf govuk_frontend_source.zip
