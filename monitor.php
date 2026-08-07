<?php

$botToken = "8831943364:AAHKaZEYWo0RKi3YJtNW_rfW9uo0vC1Em8E";
$chatId = "7844730036";

$websites = [
    [
        "nama" => "afatogel",
        "url" => "https://afatogel.com"
    ],
    [
        "nama" => "afatogelvvip",
        "url" => "https://afatogelvvip.com"
    ]
];

foreach ($websites as $site) {

    $ch = curl_init();

    curl_setopt($ch, CURLOPT_URL, $site["url"]);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_TIMEOUT, 10);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
    curl_setopt($ch, CURLOPT_USERAGENT, "Mozilla/5.0");

    curl_exec($ch);

    $status = curl_getinfo($ch, CURLINFO_HTTP_CODE);

    curl_close($ch);

    if ($status != 200) {

        $pesan =
            "🔴 Domain DOWN\n\n" .
            "Website: " . $site["nama"] . "\n" .
            "Domain: " . $site["url"] . "\n" .
            "Alasan: Tidak bisa terhubung ke server\n\n" .
            "⚠️ Segera periksa server.";

        file_get_contents(
            "https://api.telegram.org/bot{$botToken}/sendMessage?" .
            "chat_id={$chatId}&text=" . urlencode($pesan)
        );

        echo $site["nama"] . " DOWN\n";

    } else {

        echo $site["nama"] . " ONLINE\n";

    }
}